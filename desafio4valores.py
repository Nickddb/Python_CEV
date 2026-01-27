print("\033[3;45mINSERIR VALORES EM UMA TUPLA\033[m")
cont = 0
num = (int(input("Digite o 1º número: ")),
        int(input("Digite o 2º número: ")),
        int(input("Digite o 3º número: ")),
        int(input("Digite o 4º número: ")),)
print(f"Números digitados: {num}")
print(f"O número 9 apareceu \033[4;33m{num.count(9)}\033[m vezes")
if 3 in num:
    print(f"A posição do primeiro número 3 é: \033[1;32m{num.index(3)+1}\033[1;32m")
else:
    print("O valor 3 \033[1;32m não\033[m foi digitado em nenhuma posição")
for n in num:
    if n % 2 == 0:
        cont+=1
if cont == 1:
    print("O valor par digitado foi: ", end=' ')
    print(n, end=' ')
elif cont > 1:
    print("Os valores pares digitados foram: ", end=' ')
    print(n, end=' ')
else:
    print("Não houve nenhum valor par digitado")