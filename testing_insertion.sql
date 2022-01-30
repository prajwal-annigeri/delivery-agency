use del_final;

insert into employee (e_fname, e_lname, e_phone, e_admin, e_password)
values ('Prajwal', 'K P', '9987908799', true, 'kppass');



insert into customer (c_fname, c_lname, c_phone, c_address, c_covid, c_password) values
 ('Samruddh', 'A', '9875743590', '135, Kuvempunagar, Mysore', false, 'sampass');
insert into customer (c_fname, c_lname, c_phone, c_address, c_covid, c_password) values
 ('Chinmay', 'S K', '6378976577', '25, 1st cross, Vijayanagar, Mysore', false, 'chipass');
insert into customer (c_fname, c_lname, c_phone, c_address, c_covid, c_password) values
 ('Suraj', 'R', '6788854659', '69, Saraswatipuram, Mysore', true, 'surpass');
insert into customer (c_fname, c_lname, c_phone, c_address, c_covid, c_password) values
 ('Rohit', 'K', '9678558900', '122, T K Layout, Mysore', false, 'rohpass');
insert into customer (c_fname, c_lname, c_phone, c_address, c_covid, c_password) values
 ('Sanath', 'U', '9876577836', '220, Sathgalli, Mysore', true, 'sanpass');
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




insert into orders (pay_type, o_delivered, c_id, s_id, express) values ('COD', false, 1, NULL, 'Express');
insert into orders (pay_type, o_delivered, c_id, s_id, express) values ('COD', false, 1, NULL, 'Normal');
insert into orders (pay_type, o_delivered, c_id, s_id, express) values ('Prepaid', false, 2, NULL, 'Normal');
insert into orders (pay_type, o_delivered, c_id, s_id, express) values ('COD', false, 3, NULL, 'Express');
insert into orders (pay_type, o_delivered, c_id, s_id, express) values ('Prepaid', false, 3, NULL, 'Express');
insert into orders (pay_type, o_delivered, c_id, s_id, express) values ('COD', false, 4, NULL, 'Normal');
insert into orders (pay_type, o_delivered, c_id, s_id, express) values ('Prepaid', false, 5, NULL, 'Normal');
insert into orders (pay_type, o_delivered, c_id, s_id, express) values ('COD', false, 5, NULL, 'Normal');
insert into orders (pay_type, o_delivered, c_id, s_id, express) values ('COD', false, 6, NULL, 'Normal');




insert into order_product(o_id, p_id, p_qty) values (1, 2, 2);
insert into order_product(o_id, p_id, p_qty) values (1, 1, 1);
insert into order_product(o_id, p_id, p_qty) values (2, 4, 1);
insert into order_product(o_id, p_id, p_qty) values (3, 6, 1);
insert into order_product(o_id, p_id, p_qty) values (3, 8, 1);
insert into order_product(o_id, p_id, p_qty) values (4, 1, 1);
insert into order_product(o_id, p_id, p_qty) values (5, 7, 1);
insert into order_product(o_id, p_id, p_qty) values (6, 8, 2);
insert into order_product(o_id, p_id, p_qty) values (6, 2, 1);
insert into order_product(o_id, p_id, p_qty) values (7, 3, 1);
insert into order_product(o_id, p_id, p_qty) values (8, 1, 1);
insert into order_product(o_id, p_id, p_qty) values (8, 5, 1);
insert into order_product(o_id, p_id, p_qty) values (9, 3, 1);


DELIMITER $$
USE `del_final`$$
CREATE PROCEDURE `insert_employee`
(in eid integer, in fname varchar(20), in lname varchar(20), in pnum varchar(15), in passw varchar(20),
in eadmin boolean)
BEGIN
	insert into employee(e_id, e_fname, e_lname, e_phone, e_admin, e_password)
    values (eid, fname, lname, pnum, eadmin, passw);
END$$

DELIMITER ;


DELIMITER $$
USE `del_final`$$
CREATE PROCEDURE `insert_vehicle` (in vreg varchar(20), in vmodel varchar(20), in vtype varchar(20))
BEGIN
	insert into vehicle(v_reg, v_model, v_type)
    values (vreg, vmodel, vtype);
END$$

DELIMITER ;