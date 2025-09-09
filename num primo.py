print("\033[7m NÚMERO PRIMO\033[m")
num = int(input("Digite um número: "))

if num % 1 == 0 and num % num == 0:
    print("Ele é primo!")
else:
    print("Não é primo!")
