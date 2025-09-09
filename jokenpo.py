from random import randint
from time import sleep
itens = ("Pedra", "Papel", "Tesoura")
computador = randint(0,2)

print("\033[7mJOKENPO\033[m")
print('''0 - PEDRA
1 - PAPEL
2 - TESOURA''')
jogador = int(input("\nEscolha um número: "))
print("JO")
sleep(0.5)
print("KEN")
sleep(0.5)
print("PO")
print("=" * 10)
print("\033[1;31mComputador jogou {}\033[m" .format(itens[computador]))
print("\033[1;32mJogador jogou {}\033[m". format(itens[jogador]))
print("=" * 10)

if computador == 0:
    if jogador == 0:
        print("\033[1;43mEMPATOU\033[m")
    if jogador == 1:
        print("\033[1;42mJogador venceu\033[m")
    if jogador == 2:
        print("\033[1;41mComputador venceu\033[m")

if computador == 1:
    if jogador == 0:
        print("\033[1;41mComputador venceu\033[m")
    if jogador == 1:
        print("\033[1;43mEMPATOU\033[m")
    if jogador == 2:
        print("\033[1;42mJogador venceu\033[m")

if computador == 2:
    if jogador == 0:
        print("\033[1;42mJogador venceu\033[m")
    if jogador == 1:
        print("\033[1;41mComputador venceu\033[m")
    if jogador == 2:
        print("\033[1;43mEMPATOU\033[m")
