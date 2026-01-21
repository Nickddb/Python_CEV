print("\033[3;45mPAR OU ÍMPAR\033[m")
from random import randint
soma = cont = 0
while True:
    escolha = str(input("Par ou impar? ")).strip().upper()[0]
    num = int(input("Digite o valor: "))
    computador = randint(0,10)
    soma = num + computador
    print(f"Você jogou: \033[31m{num}\033[m e o computador: \033[32m{computador}\033[m, com soma de \033[36m{soma}\033[m")
    if soma % 2 == 0:
        if escolha == 'P':
            cont += 1
            print("\033[4;32mVOCÊ VENCEU!\033[m")
        elif escolha == 'I':
            print("\033[4;34mVOCÊ PERDEU!\033[m")
            False
            break
    else:
        if escolha == 'I':
            cont += 1
            print("\033[4;32mVOCÊ VENCEU!\033[m")
        elif escolha == 'P':
            print("\033[4;34mVOCÊ PERDEU!\033[m")
            False
            break
print(f"Quantidade de partidas ganhas: {cont}\n")


