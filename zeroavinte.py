tupla = ('Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis',
         'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
         'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
         'Dezenove')
num = -1
while True:
    num = int(input("Digite um número entre 0 e 20: "))
    if 0 < num < 20 :
        break
    print("Errado. Tente novamente.", end=' ')
print("\033[4;34m",tupla[num],"\033[m")
