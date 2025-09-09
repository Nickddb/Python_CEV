n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print(nome[0], 'é o seu primeiro nome')
print((nome[len(nome)-1]), 'é o seu último nome')