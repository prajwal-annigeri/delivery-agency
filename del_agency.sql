create database delivery_agency;

use delivery_agency;

create table customer (
	c_id integer primary key auto_increment,
    c_fname varchar(20) not null,
    c_lname varchar(20) not null,
    c_phone varchar(12) not null,
    c_address varchar(255) not null,
    c_covid boolean,
    c_password varchar(15) not null
);

create table employee (
	e_id integer primary key auto_increment,
    e_fname varchar(20) not null,
    e_lname varchar(20) not null,
    e_phone varchar(12) not null,
    e_admin boolean,
    e_password varchar(15) not null
);

create table product (
	p_id integer primary key auto_increment,
    p_name varchar(50) not null,
    p_retailer varchar(20) not null,
    p_type varchar(20) not null,
    p_price double not null
);

create table vehicle (
    v_reg varchar(20) not null,
    v_type varchar(20) not null,
    v_model varchar(20) not null,
    v_desc varchar(50),
	primary key(v_reg)
);

create table schedule (
	s_id integer primary key auto_increment,
    s_date date not null,
    s_completed boolean not null default 0,
    v_reg varchar(20) not null,
    e_id integer not null,
    constraint foreign key(v_reg) references vehicle(v_reg) on delete cascade on update cascade,
    constraint foreign key(e_id) references employee(e_id) on delete cascade on update cascade
);

create index idx_schedule_employee on schedule(e_id);

create index idx_schedule_vehicle on schedule(v_reg);

create table orders (
	o_id integer primary key auto_increment,
    pay_type varchar(20) not null,
    o_delivered boolean default 0,
    c_id integer not null,
    s_id integer,
    constraint foreign key(c_id) references customer(c_id) on delete cascade on update cascade,
    constraint foreign key(s_id) references schedule(s_id) on delete cascade on update cascade
);

create index idx_orders_customer on orders(c_id);
create index idx_orders_schedule on orders(s_id);

create table order_product (
	o_id integer not null,
    p_id integer not null,
    p_qty integer not null,
    primary key(o_id, p_id),
    constraint foreign key(o_id) references orders(o_id) on delete cascade on update cascade,
    constraint foreign key (p_id) references product(p_id) on delete cascade on update cascade
);

create index idx_orders_product on order_product(p_id);
    





