INSERT into disciplinas values
(1, 'portugues', 'literatura e gramatica'),
(2, 'matematica', 'algebra e geometria'),
(3, 'fisica', 'cinematica e dinamica');

INSERT into disciplinas values
(4, 'bioloca', 'botanica e ecologia');

INSERT into disciplinas values
(5, 'mecatronica', 'robotica e programacao');

select * from disciplinas;

update disciplinas set nome='biologia'
where id_disciplina=4;

copy disciplinas(id_disciplina, nome, ementa)
from  'caminho..\arquivo.csv'
delimiter ','
csv header;

create view matricula_com_sigilo as 
(
	select 
		id_matricula,
		id_aluno,
		validade
	from matricula
)

select * from matricula_com_sigilo;

--select * from disciplinas
--where nome = 'geografia'

create index idx_nome on disciplinas(nome);

select * from disciplinas
where nome = 'geografia';
