print("CAIXA ELETRÔNICO")
cinquenta = vinte = dez = um = 0
valor = int(input("Digite o valor a se sacar: "))
while True:
    if valor % 50 == 0:
        cinquenta+=1
    elif valor % 20 == 0:
        vinte+=1
    elif valor % 10 == 0:
        dez+=1
    elif valor % 1 == 0:
        um+=1
