print("\033[45mSAFE WORD\033[m")
num = cont = soma = 0
num = int(input("Digite um número [999 p/ parar]: "))
while num != 999:
    cont += 1
    soma += num
    num = int(input("Digite um número [999 p/ parar]: "))
if cont < 1:
    print("Ao total, \033[36mnenhum\033[m número foi digitado")
elif cont == 1 and cont < 2:
    print("Ao total, \033[37m1 número\033[m foi digitado.")
else:
    print("Ao total, \033[35m{} números\033[m foram digitados, com a soma entre eles sendo igual a \033[46m{}\033[m.".format(cont, soma))
