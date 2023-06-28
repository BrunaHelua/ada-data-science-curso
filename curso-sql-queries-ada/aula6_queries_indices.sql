-- estrutura de otimização - índices
-- árvore binária
select * 
from products
where category_id > 6;

create index idx_category on products(category_id)

-- util para tabelas com baixo nível de escrita, mas grande nível de leitura