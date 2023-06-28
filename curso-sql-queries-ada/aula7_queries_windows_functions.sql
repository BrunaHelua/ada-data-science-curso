-- Windows functions: funcao que gera um valor dentro de uma janela 
-- e repete esse valor na janela inteira
-- Ranqueamento
-- Agregacao
-- Posicao

-- situacao: dado funcionario, sei qual o primeiro produto que vendeu?
-- query com todos os dados que vai precisar

select 
	employee_id,
	order_date,
	first_value(order_date) over (partition by employee_id order by order_date) as first_date,
	first_value(product_name) over (partition by employee_id order by order_date) as first_product
from orders
inner join order_details on
orders.order_id = order_details.order_id
inner join products on
	products.product_id = order_details.product_id
limit 10

-- usando comando distinct - descarta linhas iguais

select distinct
	employee_id,
	first_value(order_date) over (partition by employee_id order by order_date) as first_date,
	first_value(product_name) over (partition by employee_id order by order_date) as first_product
from orders
inner join order_details on
orders.order_id = order_details.order_id
inner join products on
	products.product_id = order_details.product_id
limit 10