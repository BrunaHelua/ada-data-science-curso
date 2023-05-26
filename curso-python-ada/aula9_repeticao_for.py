# Estrutura de repeticao - forma controlada

"""for variavel in  range(5):
    print(variavel)
    
# range(start, stop[, step])
for variavel in  range(1, 6):
    print(variavel)
    
# range(start, stop[, step])
for variavel in  range(1, 13, 3):
    print(variavel)"""
    
media = 0
soma = 0
for i in range(1, 4):
    nota = float(input(f'Digite a nota {i}: '))
    soma += nota
    
media = soma / 3

print(f'A média é {media}')
    