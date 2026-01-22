print("\033[4;46mCAIXA ELETRÔNICO\033[m")
cinquenta = vinte = dez = um = 0
valor = int(input("\nDigite o valor a se sacar: "))
total = valor
ced = 50
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f"Total de {totalced} cédulas de R${ced}")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total  == 0:
            break
print("\n\033[40mBANCO FINALIZADO\033[m")
