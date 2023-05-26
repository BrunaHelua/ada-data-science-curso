# 1. O que são Funções -  abstração de ações em código, de maneira a ser reutilizada - pode ter um retorno

"""
print() # imprime mensagem no console
input() # recebe valor informado pelo usuário; pode ser armazenado em variável
len() # recebe uma lista e retorna o tamanho da lista
max() # retorna o maior elemento da lista
"""

# 2. Criação de Funções

# Função inicial

def saudacao1():
    print('Seja bem vindo')
    print('É um prazer te ver aqui')

saudacao1()

# Função com parâmetros

def saudacao(nome, curso):
    print(f'Seja bem vindo {nome}!')
    print(f'É um prazer te ver aqui no curso de {curso}')

saudacao('Bruna', 'Java')

# Função com parâmetros default
# não é obrigatório passar um nome do curso, por exemplo. Não leva a um erro
def saudacao3(nome, curso='Python'):
    print(f'Seja bem vindo {nome}!')
    print(f'É um prazer te ver aqui no curso de {curso}')

saudacao3('Bruna')

# Função com retorno

def soma(num1, num2):
    # print('Soma= ', num1, num2) # não é muito reutilizável para diferentes cenários - não se controla como a saída é feita, por exemplo, sem precisar alterar a função em si. É mais indicado, então, usar funcao com retorno
    return num1 + num2 # finaliza a função

resultado = soma(5, 7)
print('Resultado da soma é ', resultado)
    
# exemplo

def calculadora(num1, num2, operacao='+'):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        return num1 / num2
    
resultado = calculadora(15, 20)
print('Exemplo da calculadora', resultado)