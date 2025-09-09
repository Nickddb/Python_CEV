#Crie um programa que leia um num int e mostre se é par ou impar

print("ÍMPAR OU PAR")
num = int(input("Digite um número para verificar se ele é par ou ímpar: "))
if num % 2 == 0:
    print("Seu número {} é \033[1;34mpar!\033[m".format(num))
else:
    print("Seu número {} é \033[1;31mímpar!\033[m".format(num))