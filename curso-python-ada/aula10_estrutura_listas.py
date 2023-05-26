# Estrutura de dados - coleção de dados, variáveis

# Antes de lista
nota1 = 5
nota2 = 7
nota3 = 10

# com lista
notas = [7.9, 8.6, 8.2] 

# Criando listas
lista = [] # vazia
lista = list()
lista = [26, 'Bruna', 1.6, True]# aceitam diferentes tipos 
lista_de_listas = [10, [1, 2, 3]]

# Indexação e slices (fatiamento)

lista = [26, 'Bruna', 1.6, True]# aceitam diferentes tipos 

print(lista[0])
print(lista[1])
print(lista[-1]) # acessa o último elemento da lista

# Slices
lista = [10, 50, 60, 70, 250, 'elemento', True, 1200]

print(lista[0:3]) # vai até índice 3-1
print(lista[2:6:2])

# Iterações com FOR

# 1.Usando elementos da lista
for elemento in lista:
    print(elemento)
    

# 2.Usando comprimento da lista - índices

print('Comprimento da lista', len(lista))

for i in range(len(lista)):
    print(lista[i])

# Métodos de listas

lista = [1, 3, 12, 8, 2]

# append - adiciona no final
lista.append(3)
print('lista depois do append', lista)

# insert - adiciona elemento em uma posição escolhida .insert(posicao, elemento)
lista.insert(2, 10)
print('Depois do insert; ', lista)

# extend - estende lista com elementos da lista2 "concatenar elementos das listas" 

lista2 = [4, 56, 12]

lista.extend(lista2)

# pop - elimina um elemento da lista
# pode ser o último elemento ou um elemento em um posição escolhida

lista.pop()
print("lista após o pop", lista)

lista.pop(0)
print("lista após o pop na posicao zero", lista)

# remove - vai remover a primeira iteracao com o elemento escolhido

lista.remove(3)
print('Depois do remove', lista)

# count - conta a quantidade de elementos escolhidos na lista
print('Quantidade de 12', lista.count(12))

# index
print('Posição do elemento ', lista.index(12))

# sort

lista.sort(reverse=True)
print(lista)

# FUNÇÕES PARA LISTAS

# len
print('Comprimento da lista', len(lista))

# sum
print('Soma todos os elementos da lista', sum(lista))

# max
print('maior elemento da lista',len(lista))

# min
print('menor elemento da lista',min(lista))