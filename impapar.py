print("\033[4mÍMPAR OU PAR\033[m")
num = int(input("Digite um número para verificar se ele é par ou ímpar: "))
if num % 2 == 0:
    print("Seu número {} é \033[1;34mpar!\033[m".format(num))
else:
    print("Seu número {} é \033[1;31mímpar!\033[m".format(num))
