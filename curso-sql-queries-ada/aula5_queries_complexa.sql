-- queries complexas
-- boas praticas: dividir em tarefas menores

select * from order_details limit 10;

-- pedidos com quantidade maior que media

select avg(quantity) from order_details;

-- usando subqueries

select * 
from order_details
where quantity > 
	(
		select avg(quantity) 
		from order_details
	)
limit 10;

-- CTE -> Common Table Expression
-- comando with - vai 'criar uma tabela temporaria'
with average as (
	select avg(quantity) as average_quantity
	from order_details
)
select order_details.*
from order_details, average
where quantity > average.average_quantity
limit 10;
