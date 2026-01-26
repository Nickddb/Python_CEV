print("\033[3;4mLISTAGEM DE NÚMEROS\033[m\n")
from random import randint
lista = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
for l in lista:
    print(f"{l}", end= ' ')
print(f"\n\033[1;34m{max(lista)}\033[m é o maior número")
print(f"\033[1;33m{min(lista)}\033[m é o menor número")
