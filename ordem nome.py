n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print("\033[4;31m",nome[0],"\033[m", 'é o seu primeiro nome')
print("\033[4;34m",(nome[len(nome)-1]),"\033[m", 'é o seu último nome')