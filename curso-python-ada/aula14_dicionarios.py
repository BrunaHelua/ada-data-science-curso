# Dicionários- estrutura de dados chave : valor
# usa a chave para acessar ao valor

# Criando dicionários

dicio = {}
dicionario = dict()

dicio = {'nome': 'Bruna', 'idade': 27, 'altura': 1.6}

print(dicio)
print('Acessando chave idade no dicionario ', dicio['idade'])

# Adicionando elementos em um dicionario

dicio['programador'] = True # se a chave não existe, ele cria ao final do dicionario
print(dicio)

dicio['altura'] = 1.62 # se a chave já existe, ele vai reescrever o valor
print(dicio)

# Iterando sobre um dicionário
# por padrão, ele itera sobre as chaves do dicio
for chave in dicio:
    print(chave, dicio[chave])
    
# Testando a existência de uma chave

print('peso' in dicio)
print('altura' in dicio)
