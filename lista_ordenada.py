numeros = list()
for i in range(5):
    n = int(input(f"\nDigite o {i+1}º número: "))

    escolha = str(input("Quer continuar? (S/N) ")).strip().upper()
    if escolha == 'N':
        break
numeros.sort()
print(numeros)