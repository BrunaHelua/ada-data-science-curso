
# Cursos introdutórios em Data Science  

Arquivos relacionados à trilha Data Science

## Curso 1: Git e versionamento

Introdução à ferramenta Git - estou usando Git Bash para inserir comandos e GitHub para hospedar os repositórios

Conceitos:
 - HEAD: ponteiro; aponta para a branch atual

Comandos ensinados no curso:
 - git init: inicializa repositório git
 - git status: mostra estado dos arquivos em edição/no diretório a ser mapeado pelo git
 - git diff (--staged ou repo-remoto/repo-local): mostra alterações entre uma versão atual e a anterior
 - git restore (--staged) <nome-arquivo>: restaura alterações em arquivos com estado modified/staged para unmodified 
 - git add <path/arquivo-alterado>: adiciona alterações em arquivo para estado 'staged'
 - git commit -m "mensagem-sobre-commit": faz commit nas alterações e insere alterações no log
 - git remote: lista quais são os repositórios remotos que hospedam arquivos - contém o path do repo remoto
 - git push <apelido-repo-remoto> <apelido-repo-local>: 
 - git pull <apelido-repo-remoto> <apelido-repo-local>: incorpora alterações do repo remoto no repo local (faz funções de git pull e merge)
 - git fetch: mostra alterações realizadas em um repo local, mas não aplica alterações imediatamente
 - git branch: lista as branchs criadas
 - git branch nova-branch: cria nova branch
 - git checkout nome-branch: aponta o HEAD para a nome-branch (edições passam a acontecer em nome-branch)
 - git checkout -n nova-branch: cria nova branch e move HEAD para ela
 - git log: lista histórico de commits
 - git log --oneline --decorate: lista commits, mostra posição do HEAD
 - git merge nome-branch: mescla commits da nome-branch com outra branch (para onde o HEAD aponta)

## Curso 2: Cálculo básico
 - Aula 1: Definição de funções, tipos de funções e Produto cartesiano
 - Aula 2: Expressão funcional, gráficos de relações funcionais e paridade de funções
 - Aula 3: Função inversa e composição de funções
 - Aula 4: Exemplos de funções e gráficos
 - Aula 5: Conceito de limites - existência de limites, limites laterais
 - Aula 6: Exercícios
 - Aula 7: Aplicações de limites - estudo de limite de diferentes funções
 - Aula 8: Derivadas - motivação física e intuição de (de)crescimento de funções com derivadas em pontos-chave
 - Aula 9: Derivada - construção geométrica, pontos de máximo e mínimo (local e global), problemas de otimização, estudo do sinal dos pontos de ótimo com derivada de segunda ordem 
 - Aula 10: Derivada - definição e fórmulas de derivação
 - Aula 11: Regras de derivação - derivação para função linear, regra do produto, regra do quociente, regra da cadeia
 - Aula 12: Exercícios

## Curso 3: Algoritmos
 - Aula 1: O que é um algoritmo
 - Aula 2: Tipos de fluxo e criação de algoritmos
 - Aula 3: Tipos de dados (numérico, string, booleano, variável)
 - Aula 4: Estrutura de decisão - opções de escolha em um fluxo de dados
 - Aula 5: Estrutura de repetição - laços de repetição
 - Aula 6: Exercícios
 - Aula 7: Estrutura de dados Lista/Array
 - Aula 8: Criação e uso de funções
 - Aula 9: Exercício - Pseudocódigo
 - Aula 10: Desempenho de algoritmos
 - Aula 11: Dicas para montar algoritmos - boas práticas
 - Aula 12: Exercícios

## Curso 4: Python
 - Aula 1: Configurações do interpretador e IDE
 - Aula 2: Entrada e saída de dados com funções input() e print()
 - Aula 3: Criação de variáveis, reutilização e atribuição de valores às variáveis
 - Aula 4: Operadores aritméticos e booleanos
 - Aula 5: Conversão de tipos de dados usando funções
 - Aula 6: Exercícios
 - Aula 7: Estruturas condicionais - estrutura de escolha com condicionais (if-elif-else)
 - Aula 8: Controle de fluxo de execução com laço de repetição while
 - Aula 9: Controle de fluxo de execução com laço de repetição for
 - Aula 10: Estrutura de dados - tipo lista
 - Aula 11: Métodos e funções de listas
 - Aula 12: Exercícios
 - Aula 13: Criação e manipulação de funções
 - Aula 14: Estrutura de dados - tipo dicionário (chave : valor)

## Curso 5: Estatística
 - Aula 1: Introdução à estatística e amostragem
 - Aula 2: Tipos de dados, tabelas e distribuição de frequência
 - Aula 3: Visualização gráfica
 - Aula 4: Medidas de posição e medidas de dispersão (variabilidade)
 - Aula 5: Análise bidimensional
 - Aula 6: Exercícios
 - Aula 7: Regressão linear simples 
 - Aula 8: Derivadas - introdução à probabilidade
 - Aula 9: Probabilidade
 - Aula 10: Análise combinatória
 - Aula 11: Probabilidade total, parcial e Teorema de Bayes
 - Aula 12: Exercícios

## Curso 6: Banco de Dados
 - Aula 1: Introdução a banco de dados
 - Aula 2: Tipos de dados e custo do armazenamento
 - Aula 3: Modelagem de entidades
 - Aula 4: Normalização de dados
 - Aula 5: Análise bidimensional
 - Aula 6: Exercícios
 - Aula 7: Inserindo tabelas no banco 
 - Aula 8: Derivadas - introdução à probabilidade
 - Aula 9: Probabilidade
 - Aula 10: Permissionamento e Views
 - Aula 11: Índices (implementação de árvore binária)
 - Aula 12: Exercícios
## Curso 7: Introdução a SQL
 - Aula 1: Introdução ao SQL (instalação do Postgres)
 - Aula 2: Queries simples e boas práticas
 - Aula 3: Funções agregadas
 - Aula 4: Join
 - Aula 5: Queries complexas (subquery e criação de CTE)
 - Aula 6: Índices
 - Aula 7: Windows functions
 - Aula 8: PowerBI - dashboards analíticos
 - Aula 9: Filtros e métricas
 - Aula 10: PowerBI Relatório Completo