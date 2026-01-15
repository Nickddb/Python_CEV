'''Leia 2 numeros, soma, sub, mult, ou divide e aperte 5 p sair'''

print("\033[45mCALCULADORA\033[m")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

saida = False
while not saida:
    escolha = int(input("\nEscolha um:\n1- Soma\n2- Subtração\n3- Multiplicação\n4- Divisão\n5- Sair\n"))

    if escolha == 1:
        soma = num1 + num2
        print("\nA soma entre os números \033[1;46m{}\033[m e \033[1;46m{}\033[m é igual a \033[44m{}\033[m".format(num1, num2, soma))

        escolha = str(input("Deseja continuar? Digite [S/N]: ")).strip().upper()[0]
        if escolha == 'S':
            saida = False
        elif escolha == 'N':
            break
    elif escolha == 2:
        sub = num1 - num2
        print("\nA subtração entre os números \033[1;46m{}\033[m e \033[1;46m{}\033[m é igual a \033[44m{}\033[m".format(num1, num2, sub))

        escolha = str(input("Deseja continuar? Digite [S/N]: ")).strip().upper()[0]
        if escolha == 'S':
            saida = False
        elif escolha == 'N':
            break

    elif escolha == 3:
        mult = num1 * num2
        print("\nA multiplicação entre os números \033[1;46m{}\033[m e \033[1;46m{}\033[m é igual a \033[44m{}\033[m".format(num1, num2, mult))

        escolha = str(input("Deseja continuar? Digite [S/N]: ")).strip().upper()[0]
        if escolha == 'S':
            saida = False
        elif escolha == 'N':
            break

    elif escolha == 4:
        div = num1 / num2
        print("\nA divisão entre os números \033[1;46m{}\033[m e \033[1;46m{}\033[m é igual a \033[44m{}\033[m".format(num1, num2, div))

        escolha = str(input("Deseja continuar? Digite [S/N]: ")).strip().upper()[0]
        if escolha == 'S':
            saida = False
        elif escolha == 'N':
            break
    elif escolha == 5:
        break
