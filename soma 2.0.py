print("Soma entre todos os números ímpares e múltiplos de 3 num intervalo de 1 até 500")

soma = 0
cont = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        soma += i
        cont += 1
print("A soma dos \033[1;33m", cont, "\033[m números é igual a: \033[1;34m", soma,'\033[m')