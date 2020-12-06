from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_session import Session
import mysql.connector
import secrets

con = mysql.connector.connect(
    user=secrets.dbusername__,
    password=secrets.dbpassword__,
    host=secrets.dbhost__,
    database=secrets.dbname__
)

cur = con.cursor(buffered=True)

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
app.jinja_env.filters['zip'] = zip


@app.route('/')
def index():
    message = request.args.get('message')
    session['stamp'] = None

    if message:
        return render_template('index.html', text=message)
    else:
        return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return redirect('/')
    if request.method == 'POST':
        uid = request.form.get('userid_val')
        passw = request.form.get("password_val")
        role = request.form.get("role")
        if role == "customer":
            cur.execute(
                'SELECT * FROM customer WHERE c_id=%s AND c_password=%s', (uid, passw))
            match = cur.fetchone()

            if match:
                session["stamp"] = f'c{uid}'
                session["fname"] = match[1]
                session["lname"] = match[2]
                session['admin'] = 0
                print(session["stamp"])
                return redirect(url_for('customer_login'))
            else:
                return redirect(url_for('index', message='Invalid credentials'))

        elif role == "employee":
            cur.execute(
                'SELECT * FROM employee WHERE e_id=%s AND e_password=%s', (uid, passw))
            match = cur.fetchone()
            # print("WORKING")
            if match:
                # print(match[4])
                session["stamp"] = f'e{uid}'
                session["fname"] = match[1]
                session["lname"] = match[2]
                if match[4] == 1:
                    session['admin'] = 1
                else:
                    session['admin'] = 0
                if match[4] == 1:
                    print("WORKING")
                    return redirect(url_for('add_employee'))
                else:
                    return redirect(url_for('normal_emp'))
            else:
                return redirect(url_for('index', message='Invalid credentials'))

        else:
            return redirect(url_for('index', message='Invalid credentials'))


@app.route('/customer_login')
def customer_login():
    if session['stamp']:
        if session['stamp'][0] == 'c':
            stampid = int(session['stamp'][1:])
            # print(stampid)
            # print("Working")
            # cur.execute("SELECT * FROM customer WHERE c_id=%s",
            #             (stampid,))
            # fname = cur.fetchone()
            cur.execute(
                "SELECT orders.o_id, schedule.s_id, employee.e_id, s_date, e_phone, e_fname, pay_type\
                     FROM orders, schedule, employee\
                     WHERE orders.s_id= schedule.s_id and schedule.e_id = employee.e_id and c_id = %s and o_delivered = 0", (stampid, ))
            orders_on_schedule = cur.fetchall()
            # print(orders_on_schedule)

            order_amounts = []
            for order in orders_on_schedule:
                cur.execute("select total_amount\
                    FROM\
                        (\
                            select o_id, sum(amt) as Total_amount\
                                FROM\
                                    (\
                                        select order_product.o_id, order_product.p_id, order_product.p_qty,\
                                             product.p_price, product.p_price*order_product.p_qty as amt\
                                            from order_product\
                                                inner join product on order_product.p_id=product.p_id) as T\
                                                    group by o_id)as T where o_id=%s;", (order[0], ))
                order_amounts.append(cur.fetchone()[0])

            # print(order_amounts)

            order_details_list = []

            for order_details, order_amt in zip(orders_on_schedule, order_amounts):
                # print(order_details, order_amt)
                order_details_list_temp = list(order_details)
                order_details_list_temp.append(order_amt)
                order_details_list.append(order_details_list_temp)
                # print(order_details_list)

            # print(list_of_orders)

            cur.execute(
                "SELECT o_id, pay_type FROM orders WHERE c_id = %s AND o_delivered = 0 and s_id IS NULL", (stampid,))
            orders_not_on_schedule = cur.fetchall()
            # print(orders_not_on_schedule)

            order_amounts_not = []

            for order in orders_not_on_schedule:
                cur.execute("select total_amount\
                    FROM\
                        (\
                            select o_id, sum(amt) as Total_amount\
                                FROM\
                                    (\
                                        select order_product.o_id, order_product.p_id, order_product.p_qty,\
                                             product.p_price, product.p_price*order_product.p_qty as amt\
                                            from order_product\
                                                inner join product on order_product.p_id=product.p_id) as T\
                                                    group by o_id)as T where o_id=%s;", (order[0], ))
                order_amounts_not.append(cur.fetchone()[0])

            order_details_list_nonscheduled = []

            for order_details, order_amt in zip(orders_not_on_schedule, order_amounts_not):
                # print(order_details, order_amt)
                order_details_list_temp_non = list(order_details)
                # print(order_details_list_temp_non)
                order_details_list_temp_non.append(order_amt)
                # print(order_details_list_temp_non)
                order_details_list_nonscheduled.append(
                    order_details_list_temp_non)
                # print(order_details_list_nonscheduled)

           # print(order_amounts_not)

            return render_template('customer_login.html', orders_on_schedule=order_details_list,
                                   orders_not_on_schedule=order_details_list_nonscheduled,
                                   first_name=session['fname'], last_name=session['lname'])
        else:
            return redirect(url_for('index'))

    else:
        return redirect(url_for('index'))


@app.route('/logout')
def logout():
    session['stamp'] = None
    session['fname'] = None
    session['lname'] = None
    session['admin'] = None
    session['date'] = None
    return redirect(url_for('index'))


@app.route('/add_schedule')
def add_schedule():
    if session['stamp']:
        if session['stamp'][0] == 'e':
            stampid = int(session['stamp'][1:])
            # cur.execute(
            #     "SELECT * FROM employee WHERE e_id=%s", (stampid,))
            # match = cur.fetchone()

            if session['admin'] == 1:
                return render_template('add_schedule.html', first_name=session['fname'], last_name=session['lname'])
            else:
                return redirect(url_for('logout'))
        else:
            return redirect(url_for('logout'))
    else:
        return redirect(url_for('logout'))


@app.route('/add_vehicle')
def add_vehicle():
    if session['stamp']:
        if session['stamp'][0] == 'e':
            stampid = int(session['stamp'][1:])
            # cur.execute(
            #     "SELECT * FROM employee WHERE e_id=%s", (stampid,))
            # match = cur.fetchone()

            if session['admin'] == 1:
                return render_template('add_vehicle.html', first_name=session['fname'], last_name=session['lname'])
            else:
                return redirect(url_for('logout'))
        else:
            return redirect(url_for('logout'))
    else:
        return redirect(url_for('logout'))


@app.route('/add_employee')
def add_employee():
    if session['stamp']:
        if session['stamp'][0] == 'e':
            stampid = int(session['stamp'][1:])
            # cur.execute(
            #     "SELECT * FROM employee WHERE e_id=%s", (stampid,))
            # match = cur.fetchone()

            if session['admin'] == 1:
                return render_template('add_employee.html', first_name=session['fname'], last_name=session['lname'])
            else:
                return redirect(url_for('logout'))
        else:
            return redirect(url_for('logout'))
    else:
        return redirect(url_for('logout'))


@ app.route('/normal_emp')
def normal_emp():
    if session['stamp']:
        if session['stamp'][0] == 'e':
            stampid = int(session['stamp'][1:])

            con.commit()
            cur.execute(
                "SELECT s_id, s_date, v_reg FROM schedule WHERE e_id=%s AND s_completed=0", (stampid,))
            s_ids = cur.fetchall()
            # print(s_ids)
            s_ids_list = []

            for s_tuple in s_ids:
                # print(s_tuple)
                # print(type(s_tuple))
                s_ids_list.append(s_tuple)

            # print("LLOOOKKK")
            # print(s_ids_list)
            s_orders_lists = []
            for s_id in s_ids_list:

                cur.execute(
                    "SELECT o_id, pay_type, c_fname, c_lname, c_phone, c_address, c_covid, express\
                        FROM orders INNER JOIN customer ON orders.c_id=customer.c_id\
                            WHERE s_id=%s AND o_delivered=0", (s_id[0], ))
                orders_of_schedule = cur.fetchall()
                # print("HERE")
                # print(orders_of_schedule)
                s_orders_lists.append(orders_of_schedule)

            # print(s_orders_lists)

            zipped_id_orders = zip(s_ids_list, s_orders_lists)

            # for i in zipped_id_orders:
            # print("HEREZIP")
            # print(i)

            # print(s_orders_lists)

            return render_template('normal_emp.html', first_name=session['fname'], last_name=session['lname'],
                                   zipped_id_orders=zipped_id_orders, s_ids_list=s_ids_list, s_orders_lists=s_orders_lists)
        else:
            return redirect(url_for('logout'))
    else:
        return redirect(url_for('logout'))


@app.route('/vehicle_added', methods=["POST", "GET"])
def vehicle_added():

    if request.method == 'GET':
        return redirect(url_for('add_vehicle'))
    if request.method == 'POST':
        # print("WORKING")
        vreg = request.form.get("vreg").upper()
        vmodel = request.form.get("vmodel")
        vtype = request.form.get("vtype")
        cur.execute("SELECT v_reg FROM vehicle")
        vregs = cur.fetchall()
        vregs_list = []
        for i in vregs:
            vregs_list.append(i[0])
        # print(vregs_list)
        if vreg in vregs_list:
            flash('Vehicle already exists')
            print(vreg, vmodel, vtype)
            return redirect(url_for('add_vehicle'))
        else:
            # print('Added')
            cur.execute("CALL insert_vehicle(%s, %s, %s)",
                        (vreg, vmodel, vtype))
            con.commit()
            print(vreg, vmodel, vtype)
            return render_template('vehicle_added.html', id_val=vreg)


@app.route('/employee_added', methods=["POST", "GET"])
def employee_added():

    if request.method == 'GET':
        return redirect(url_for('add_employee'))
    if request.method == 'POST':
        # print("WORKING")
        eid = int(request.form.get("eid"))
        efname = request.form.get("efname").title()
        elname = request.form.get("elname").title()
        ephone = request.form.get("ephone")
        if not efname.isalpha():
            flash('Enter proper first name')
            return redirect(url_for('add_employee'))
        if not elname.isalpha():
            flash('Enter proper last name')
            return redirect(url_for('add_employee'))
        if not ephone.isnumeric():
            flash('Enter proper phone number')
            return redirect(url_for('add_employee'))
        epassword = request.form.get("epassword")
        eadmin = request.form.get("admin")
        if eadmin == "Admin":
            eadmin = 1
        else:
            eadmin = 0
        cur.execute("SELECT e_id FROM employee")
        eids = cur.fetchall()
        eids_list = []
        for i in eids:
            eids_list.append(i[0])
        # print(eids_list)
        if eid in eids_list:
            flash('Employee ID already exists')
            print(eid, efname, elname, ephone, epassword)
            return redirect(url_for('add_employee'))
        else:

            cur.execute("CALL insert_employee(%s, %s, %s, %s, %s, %s)",
                        (eid, efname, elname, ephone, epassword, eadmin))
            con.commit()
            print(eid, efname, elname, ephone, epassword, eadmin)
            return render_template('employee_added.html', id_val=eid)


@app.route('/customer_orders')
def customer_orders():
    if session['stamp']:
        if session['stamp'][0] == 'c':
            stampid = int(session['stamp'][1:])
            cur.execute(
                "SELECT orders.o_id, product.p_name, order_product.p_qty, order_product.p_qty*product.p_price\
                    FROM orders INNER JOIN order_product ON orders.o_id = order_product.o_id\
                        INNER JOIN product on order_product.p_id=product.p_id where o_delivered = 0 AND c_id=%s;",
                (stampid,))
            orders = cur.fetchall()
            # print(orders)

            return render_template('customer_orders.html', first_name=session['fname'], last_name=session['lname'],
                                   orders=orders)
        else:
            return redirect(url_for('logout'))
    else:
        return redirect(url_for('logout'))


@app.route('/delivery_done', methods=['POST', 'GET'])
def delivery_done():
    if request.method == "GET":
        return redirect('/normal_emp')
    if request.method == "POST":
        oid_done = request.form.get("id_of_delivered")
        sched_check = request.form.get("schedule_check")
        cur.execute('SELECT s_id from schedule where e_id=%s',
                    (session['stamp'][1:],))

        scheds = cur.fetchall()
        # print(oid_done)
        # print(sched_check)
        cur.execute(
            "UPDATE orders SET o_delivered=1 WHERE o_id=%s", (oid_done,))
        con.commit()
        sched_list = []
        for sched in scheds:
            sched_list.append(sched[0])

        for sched in sched_list:
            cur.execute("UPDATE schedule SET s_completed=1\
                where s_id=%s AND NOT EXISTS(SELECT o_id FROM orders WHERE s_id =%s AND o_delivered=0)",
                        (sched, sched))
            con.commit()

        return redirect('normal_emp')


@app.route('/date_selected', methods=['GET', 'POST'])
def date_selected():
    if request.method == "GET":
        return redirect('/add_schedule')
    if request.method == "POST":
        date_selected = request.form.get('schedule_date')
        session['date'] = date_selected
        print(date_selected)
        cur.execute('SELECT e_id FROM employee WHERE e_id NOT IN\
            (SELECT e_id FROM schedule WHERE s_date=%s) AND e_admin=0', (date_selected, ))
        eid_tuples = cur.fetchall()
        available_eids = []
        for eid in eid_tuples:
            available_eids.append(eid[0])
        print(available_eids)

        cur.execute('SELECT v_reg FROM vehicle WHERE v_reg NOT IN\
            (SELECT v_reg FROM schedule WHERE s_date=%s)', (date_selected, ))
        vreg_tuples = cur.fetchall()
        # print(vreg_tuples)
        available_vregs = []
        for vreg in vreg_tuples:
            available_vregs.append(vreg[0])
        print(available_vregs)

        cur.execute(
            "SELECT o_id, express FROM orders WHERE s_id IS NULL AND o_delivered=0")
        orders_available = cur.fetchall()
        print(orders_available)

        return render_template('date_selected.html', date=date_selected, available_eids=available_eids,
                               available_vregs=available_vregs, first_name=session[
                                   'fname'], last_name=session['lname'],
                               orders_available=orders_available)


@app.route('/schedule_added', methods=['GET', 'POST'])
def schedule_added():
    if request.method == 'GET':
        return redirect('/add_schedule')
    if request.method == 'POST':
        sid_set = request.form.get('set_id')
        cur.execute("SELECT s_id FROM schedule")
        existing_sids = cur.fetchall()
        existing_sids_list = []
        for i in existing_sids:
            existing_sids_list.append(i[0])
        print("HERE")
        print(existing_sids_list)
        if int(sid_set) in existing_sids_list:
            flash('Schedule ID already exists')
            return redirect('/add_schedule')
        eid_selected = request.form.get('emp_id')
        vreg_selected = request.form.get('v_reg')
        oids_selected = request.form.getlist('order_checkbox')
        print(sid_set)
        print(eid_selected)
        print(vreg_selected)
        print(oids_selected)
        cur.execute('INSERT INTO schedule(s_id, s_date, s_completed, v_reg, e_id)\
             VALUES (%s, %s, %s, %s, %s)', (sid_set, session['date'], 0, vreg_selected, eid_selected))
        con.commit()

        for order in oids_selected:
            cur.execute("UPDATE orders SET s_id=%s WHERE o_id=%s",
                        (sid_set, order))
            con.commit()
        return render_template('schedule_added.html')


@app.route('/show_employees')
def show_employees():
    if session['stamp']:
        if session['stamp'][0] == 'e':
            stampid = int(session['stamp'][1:])
            # cur.execute(
            #     "SELECT * FROM employee WHERE e_id=%s", (stampid,))
            # match = cur.fetchone()

            if session['admin'] == 1:
                cur.execute(
                    "SELECT e_id, e_fname, e_lname, e_phone, e_admin FROM employee")
                employees = cur.fetchall()
                return render_template('show_employees.html',
                                       employees=employees, first_name=session['fname'], last_name=session['lname'])
            else:
                return redirect(url_for('logout'))
        else:
            return redirect(url_for('logout'))
    else:
        return redirect(url_for('logout'))


if __name__ == "__main__":
    app.debug = True
    app.run()
