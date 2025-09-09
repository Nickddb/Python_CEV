print("\033[7mCOMPARAR 2 NÚMEROS\033[m")
num1 = float(input("Digite o 1º número: "))
num2 = float(input("Digite o 2º número: "))

if num1 > num2:
    print("O número \033[4;33m{}\033[m é maior que o número \033[4;36m{}\033[m".format(num1,num2))
elif num2 > num1:
    print("O número \033[4;36m{}\033[m é maior que o número \033[4;33m{}\033[m".format(num2, num1))
else:
    print("\033[1;35mAmbos os números são iguais!\033[m")
