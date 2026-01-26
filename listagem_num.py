print("\033[3;4mLISTAGEM DE NÚMEROS\033[m\n")
from random import randint
maior = menor = 0
for l in range(0,5):
    lista = randint(0,10)
    lista += lista
    print(lista, end= ' ')
    if lista > maior:
        maior = lista
    elif lista < menor:
        menor = lista
print(f"\n\033[1;34m{maior}\033[m é o maior número")
print(f"\033[1;33m{menor}\033[m é o menor número")
