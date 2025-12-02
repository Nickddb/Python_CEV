print("MAIOR PESO")
maior = 0
menor = 0

for p in range(0,3):
    peso = float(input(f"Digite o peso da {p+1}ª pessoa: "))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print("O maior peso foi de: ", maior, " kg")
print("O menor peso foi de: ", menor, " kg")