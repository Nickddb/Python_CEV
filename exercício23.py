num = int(input("Digite um número até 9999: "))
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10
print('=' * 12)
print("Unidade: ", unidade)
print("Dezena: ", dezena)
print("Centena: ", centena)
print("Milhar: ", milhar)
print('=' * 12)
