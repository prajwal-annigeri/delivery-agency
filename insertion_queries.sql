use delivery_agency;


insert into employee (e_fname, e_lname, e_phone, e_admin, e_password) values ('Prajwal', 'K P', '9987908799', true, 'kppass');
insert into employee (e_fname, e_lname, e_phone, e_admin, e_password) values ('Nagaraj', 'H', '9945308799', true, 'nagpass');
insert into employee (e_fname, e_lname, e_phone, e_admin, e_password) values ('Sankalp', 'K', '9564788799', true, 'sankpass');
insert into employee (e_fname, e_lname, e_phone, e_admin, e_password) values ('Akshay', 'B', '7687908799', false, 'akspass');
insert into employee (e_fname, e_lname, e_phone, e_admin, e_password) values ('Abhishek', 'B', '6387908799', false, 'abhipass');
insert into employee (e_fname, e_lname, e_phone, e_admin, e_password) values ('Vikas', 'B', '8707908799', false, 'vikpass');
insert into employee (e_fname, e_lname, e_phone, e_admin, e_password) values ('Akshay', 'B', '7687908799', false, 'akspass');
insert into employee (e_fname, e_lname, e_phone, e_admin, e_password) values ('Ganesh', 'M', '9800908799', false, 'ganpass');
insert into employee (e_fname, e_lname, e_phone, e_admin, e_password) values ('Anush', 'B', '9986908799', false, 'anupass');

 

insert into vehicle (v_reg, v_type, v_model) values ('KA09EF2135', 'Motorcycle',  'Honda Shine');
insert into vehicle (v_reg, v_type, v_model) values ('KA09MB6123', 'Scooter',  'Honda Activa');
insert into vehicle (v_reg, v_type, v_model) values ('KA09EF3261', 'Motorcycle',  'Discover');
insert into vehicle (v_reg, v_type, v_model) values ('KA09AB3489', 'Scooter',  'Honda Activa');
insert into vehicle (v_reg, v_type, v_model) values ('KA09DC2138', 'Motorcycle',  'Bajaj Dominar');
insert into vehicle (v_reg, v_type, v_model) values ('KA09FE8743', 'Motorcycle',  'TVS Jupiter');



insert into customer (c_fname, c_lname, c_phone, c_address, c_covid, c_password) values
 ('Samruddh', 'A', '9875743590', '135, Kuvempunagar, Mysore', false, 'sampass');
insert into customer (c_fname, c_lname, c_phone, c_address, c_covid, c_password) values
 ('Chinmay', 'S K', '6378976577', '25, 1st cross, Vijayanagar, Mysore', false, 'chipass');
insert into customer (c_fname, c_lname, c_phone, c_address, c_covid, c_password) values
 ('Suraj', 'R', '6788854659', '69, Saraswatipuram, Mysore', true, 'surpass');
insert into customer (c_fname, c_lname, c_phone, c_address, c_covid, c_password) values
 ('Rohit', 'K', '9678558900', '122, T K Layout, Mysore', false, 'rohpass');
insert into customer (c_fname, c_lname, c_phone, c_address, c_covid, c_password) values
 ('Sanath', 'U', '9876577836', '220, Sathgalli, Mysore', true, 'sampass');
insert into customer (c_fname, c_lname, c_phone, c_address, c_covid, c_password) values
 ('Adnan', 'B', '9987098754', '122, VV Mohalla, Mysore', false, 'adnpass');
insert into customer (c_fname, c_lname, c_phone, c_address, c_covid, c_password) values
 ('Anuj', 'T', '9879098754', '25, Bannimantap, Mysore', false, 'anupass');
 



insert into product(p_name, p_retailer, p_type, p_price) values ('HP M30', 'Flipkart', 'Mouse', 400);
insert into product(p_name, p_retailer, p_type, p_price) values ('Adidas Duramo', 'Amazon', 'Shoes', 2000);
insert into product(p_name, p_retailer, p_type, p_price) values ('OnePlus 8', 'Amazon', 'Mobile Phone', 40000);
insert into product(p_name, p_retailer, p_type, p_price) values ('Logitech G30', 'Flipkart', 'Mouse', 1200);
insert into product(p_name, p_retailer, p_type, p_price) values ('Nike FreeRN', 'Myntra', 'Shoes', 2100);
insert into product(p_name, p_retailer, p_type, p_price) values ('Titan G212', 'Myntra', 'Watch', 1300);
insert into product(p_name, p_retailer, p_type, p_price) values ('Sony M300', 'Flipkart', 'Speakers', 2000);
insert into product(p_name, p_retailer, p_type, p_price) values ('Boat 300', 'Amazon', 'Speakers', 1500);
insert into product(p_name, p_retailer, p_type, p_price) values ('Samsung Note 10', 'Flipkart', 'Mobile Phone', 38000);
insert into product(p_name, p_retailer, p_type, p_price) values ('RedGear A15', 'Flipkart', 'Mouse', 500);

insert into schedule (s_date, s_completed, v_reg, e_id) values ('2020-11-30', true, 'KA09EF2135', 4);
insert into schedule (s_date, s_completed, v_reg, e_id) values ('2020-11-30', true, 'KA09MB6123', 5);
insert into schedule (s_date, s_completed, v_reg, e_id) values ('2020-12-01', false, 'KA09EF3261', 6);
insert into schedule (s_date, s_completed, v_reg, e_id) values ('2020-11-01', false, 'KA09AB3489', 5);



insert into orders (pay_type, o_delivered, c_id, s_id) values ('COD', true, 1, 1);
insert into orders (pay_type, o_delivered, c_id, s_id) values ('Prepaid', true, 2, 2);
insert into orders (pay_type, o_delivered, c_id, s_id) values ('COD', false, 3, 3);
insert into orders (pay_type, o_delivered, c_id, s_id) values ('Prepaid', false, 4, 4);


insert into order_product (o_id, p_id, p_qty) values (1, 2, 1);
insert into order_product (o_id, p_id, p_qty) values (1, 3, 1);
insert into order_product (o_id, p_id, p_qty) values (2, 3, 1);
insert into order_product (o_id, p_id, p_qty) values (2, 5, 2);
insert into order_product (o_id, p_id, p_qty) values (3, 7, 1);
insert into order_product (o_id, p_id, p_qty) values (3, 9, 1);
insert into order_product (o_id, p_id, p_qty) values (4, 4, 2);
insert into order_product (o_id, p_id, p_qty) values (4, 3, 1);
