print("\033[45mMÉDIA WHILE\033[m")
soma = media = num3 = 0
cont = 2
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
escolha = int(input("\nDeseja continuar?\n\033[4m0- Não\033[m\n\033[4m1- Sim\033[m\n"))
while escolha != 0:
    num3 = int(input("Digite o {}º número: ".format(cont + 1)))
    soma = num3 + num1 + num2
    cont += 1
    if escolha == 0:
        soma = num1 + num2
        num3 = num1
        break
    elif escolha != 1 or escolha != 0:
        print("RESPONDER ENTRE 1 OU 0")
    escolha = int(input("\nDeseja continuar?\n\033[4m0- Não\033[m\n\033[4m1- Sim\033[m\n"))
media = soma / cont
if num1 > num2 and num1 > num3 :
    print("\033[2;34m",num1,"\033[m é o maior número e", end=' ')
elif num2 > num1 and num2 > num3:
    print("\033[2;34m", num2, "\033[m é o maior número e", end=' ')
else:
    print("\033[2;34m", num3, "\033[m é o maior número e", end=' ')
if num1 < num2 and num1 < num3:
    print("\033[2;35m", num1, "\033[m é o menor número")
elif num2 < num1 and num2 < num3:
    print("\033[2;35m", num2, "\033[m é o menor número")
else:
    print("\033[2;35m", num3, "\033[m é o menor número")
print("Media: ", media)
