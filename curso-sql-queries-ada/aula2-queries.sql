select * from products
limit 10;

select 
	product_name,
	unit_price,
	units_in_stock,
	units_in_stock * unit_price as total_revenue
from products
limit 10;

select * from employees
where city = 'Seattle'
limit 10;

select * from employees
where hire_date >= '1993-01-01'
limit 10;

select * from employees
where first_name like 'M%'
limit 10;

select * from employees
where title like '%Sales%'
limit 10;

select *, unit_price * quantity as revenue
from order_details
limit 10;