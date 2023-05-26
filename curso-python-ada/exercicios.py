cont = 0
resultado = 0
n = 1000

while cont != n:

    resultado = resultado + 1/(2**cont)

    cont = cont + 1

print(resultado)

"""for _ in range(10):

    print("Olá, mundo!")
"""
for _ in [10]:
    print("Olá, mundo!")

lista_inicial = [10, 5, -7, 6, -42, 63, -8, -5, 13]

lista_final = []

for item in lista_inicial:

    if item % 2 == 0:

        if item < 0:

            lista_final.append(-item)
    
        else:

            lista_final.append(item)
    else:

        if item < 0:
            
            lista_final.append(-2*item)
    
        else:

            lista_final.append(2*item)
            
# LISTA-FINAL 10, 10, 14, 6, 42, 126, 8, 10, 26