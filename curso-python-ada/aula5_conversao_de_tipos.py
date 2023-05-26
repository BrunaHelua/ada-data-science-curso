# Conversão de tipos
# Python tem tipagem forte e dinâmica (capaz de inferir o tipo da variável automaticamente)

idade = '26' 

print(idade, type(idade))

idade_inteira = int(idade)

print(idade_inteira, type(idade_inteira))

# int()
# str()
# float()
# bool()

# input recebe qualquer valor, mas a leitura é guardada como str

altura = float(input('Informe a altura: '))
print(altura, type(altura))

x = 4.2

y = 10

z = "42"

print(not (((x * y == z) and not (x < y)) or y % 2 == 0))
print(not (((not True) or int(z) % 7 == 0) and ((str(int(x*y)) == z) and (type(x) != type(z)))))