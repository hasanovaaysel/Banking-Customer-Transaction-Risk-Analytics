create database banking_analytics_db;
use banking_analytics_db;
create table customers(
customer_id int primary key,
customer_name varchar(100) not null,
gender varchar(20),
date_of_birth date,
city varchar(50),
customer_segment varchar(30),
signup_date date,
customer_status varchar(20)
); drop table customers;
create table branches(
branch_id int primary key,
branch_name varchar(100) not null,
city varchar(50),
branch_type varchar(30),
opening_date date
); 
SELECT *FROM branches;
create table employees(
employee_id int primary key,
employee_name varchar(100),
branch_id int,
role varchar(50),
hire_date date,
employee_status varchar(50),
foreign key(branch_id) references branches(branch_id)
);
SELECT COUNT(*) FROM customers;
create table accounts(
account_id int primary key,
customer_id int not null,
branch_id int not null,
account_type varchar(30),
opening_date date,
current_balance decimal(10,2),
account_status varchar(20),
foreign key(customer_id)references customers(customer_id),
foreign key(branch_id) references branches(branch_id)
); 


create table transaction(
transaction_id int primary key,
account_id int not null,
transaction_date datetime,
transaction_type varchar(20),
amount decimal(10,2),
transaction_status varchar(30),
channel varchar(30),
merchant_category varchar(50),
foreign key(account_id)references accounts(account_id)
); 
drop table transaction;
SELECT COUNT(*) FROM transaction;
create table loans(
loan_id int primary key,
customer_id int not null,
loan_type varchar(50),]
loan_amount decimal(10,2),
loan_status varchar(20),
interest_rate decimal(10,2),
issue_date date,
maturity_date date,
foreign key(customer_id) references customers(customer_id)
);

create table loan_payments(
payment_id int primary key,
loan_id int not null,
payment_date date,
payment_amount decimal(10,2),
payment_status varchar(20),
foreign key(loan_id)references loans(loan_id)
);

create table cards(
card_id int primary key,
customer_id int not null,
account_id int not null,
card_type varchar(20),
card_network varchar(20),
issue_date date,
expiry_date date,
card_status varchar(20),
foreign key(customer_id)references customers(customer_id),
foreign key(account_id) references accounts(account_id)
);

create table complaints(
complaint_id int primary key,
customer_id int not null,
branch_id int not null,
complaint_date date,
complaint_category varchar(50),
complaint_status varchar(30),
resolution_days int,
foreign key(customer_id) references customers(customer_id),
foreign key(branch_id) references branches(branch_id) 
);
create table campaigns(
campaign_id int primary key,
campaign_name varchar(100),
campaign_type varchar(50),
channel varchar(30),
start_date date,
end_date date,
campaign_budget decimal(15,2),
campaign_status varchar(20)
);

select Count(*) as total_customers from customers;
select Count(*) as total_branches  from branches;
select Count(*) as total_employees  from employees;
select Count(*) as total_accounts  from accounts;
select Count(*) as total_transactions  from transaction;
select Count(*) as total_loans from loans;

select customer_id,count(*) as dublicate_count
from customers
group by customer_id
having count(*)>1;

select 
	count(*) as total_rows,
    count(customer_id) as customers_id,
    count(customer_name) as customer_names,
    count(city) as cities,
    count(customer_segment) as segments
from customers;

select count(*) as invalid_accounts from accounts a
left join customers c
on a.customer_id=c.customer_id
where c.customer_id is null;

select customer_segment,count(*) as customer_count
from customers
group by customer_segment
order by customer_count desc;

SELECT
    c.customer_segment,
    COUNT(DISTINCT c.customer_id)
        AS customer_count,
    SUM(a.current_balance)
        AS total_balance,
    AVG(a.current_balance)
        AS average_balance
FROM customers c
LEFT JOIN accounts a
    ON c.customer_id = a.customer_id
GROUP BY c.customer_segment
ORDER BY total_balance DESC;


select customer_segment,
count(distinct c.customer_id) as customer_count,
sum(a.current_balance) as total_balance,
avg(a.current_balance) as average_balance
from customers c
left join accounts a
on c.customer_id=a.customer_id
group by customer_segment
order by total_balance desc;


select c.customer_id,c.customer_name,c.customer_segment,
sum(a.current_balance) as total_balance from customers c
join accounts a 
on c.customer_id=a.customer_id
group by c.customer_id,c.customer_name,c.customer_segment
order by total_balance desc
limit 10;
















