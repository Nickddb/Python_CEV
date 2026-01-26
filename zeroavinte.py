tupla = 'Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte'
num = -1
while num < 0 or num > 20:
    num = int(input("Digite um número entre 0 e 20: "))
    if num >= 0 and num <= 20:
        print("\033[4;34m",tupla[num],"\033[m")
    elif num < 0 or num > 20 :
        print("Errado. Tente novamente.", end=' ')