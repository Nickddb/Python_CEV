numeros = list()
while True:
    n = int(input(f"\nDigite um número: "))
    if n not in numeros:
        numeros.append(n)
        print("Valor adicionado")
    else:
        print("Valor duplicado")

    escolha = str(input("Quer continuar? (S/N) ")).strip().upper()
    if escolha == 'N':
        break
numeros.sort()
print(numeros)