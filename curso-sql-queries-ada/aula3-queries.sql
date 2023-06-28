 -- funcoes agregadas
 -- contagem
 -- soma
 -- media
 -- maximo
 -- minimo
 
 select * from order_details limit 10;
 select sum(quantity) as total_units_sold
 from order_details;
 
 -- situacao: quantas unidades de cada produto foram vendidas?
 -- usando agrupamentos usando alguma coluna para representar
 select product_id, sum(quantity) as total_units_sold
 from order_details
 group by product_id
 order by total_units_sold desc
 limit 10;
 
 -- situacao: vendas por mes -- count vai retornar o n de linhas que satisfazem
 -- as condicoes
select date_trunc('month', order_date) as order_month, count(order_id)
from orders
group by order_month
order by order_month
limit 10;
 
-- funcao date_trunc('intervalo de tempo', coluna)

select product_id, sum(quantity) as total_units_sold
from order_details
group by product_id
having sum(quantity) >= 1000 -- filtra depois do agrupamento
limit 10;

 
 
 
 
 