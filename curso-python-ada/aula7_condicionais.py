# Estruturas condicionais

idade = 20

if idade >= 18:
    print('Você é maior de idade')
else:
    print('Você é menor de idade')
    
"""
Situação: imprimir 'aprovado' caso estudante tenha media maior igual a 7, reprovado para média menor que 7
"""
# media = float(input('Digite a media do estudante: '))
nota1 = 6
nota2 = 5
presenca = 100

media = (nota1+nota2) / 2 

if media >= 7 and presenca >= 70:
    print('Aprovado')
else:
    print('Reprovado')
    
"""
if  media >= 7:
    print('A media é: ', media, '. Aprovado')
elif media >= 5:
    print('A media é', media, 'Está em recuperação')
else:
    print('A media é: ', media, '. Reprovado')"""