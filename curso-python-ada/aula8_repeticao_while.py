# Estruturas de repeticao - While

numero_sorteado = 15

numero_escolhido = int(input('Informe um número entre 1 e 20: '))

# repetições não controladas - sem o contador
while numero_sorteado != numero_escolhido:
    print('Você ERROU. Tente novamente')
    numero_escolhido = int(input('Informe um número entre 1 e 20: '))

print('Você acertou!')

# repetições controladas - usando o contador
contador = 0
while contador < 5:
    print(contador)
    contador += 1