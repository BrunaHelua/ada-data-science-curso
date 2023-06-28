-- estudo da funcao join

select * from products;

select 
	product_name,
	quantity_per_unit,
	unit_price,
	category_name,
	description
from products
inner join categories ON 
categories.category_id = products.category_id
limit 10;

-- desafio: juntar pelo fornecedor supplier