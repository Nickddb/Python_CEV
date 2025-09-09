#Escreva um programa que faça o computador pensar
#em um num inteiro entre 0 e 5 e peça para o usuário tentar
#descobrir qual foi o num escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu

from random import randint

compiuter = randint(0,5)
print("JOGUINHO DE ADIVINHAÇÃO \nAdivinhe um número entre 0 e 5")
jogador = int(input("O computador pensou em um número. Digite qual número ele pensou: "))

if jogador == compiuter:
    print("\033[1;32mParabéns! Você acertou!\033[m")
elif jogador > 5 or jogador < 0:
    print("\033[7mEu falei pra escolher um número entre 0 e 5 apenas!\033[m")
elif jogador != compiuter:
    print("\033[1;31mErrou! :(\033[m o computador pensou no número \033[4;32m{}\033[m e não no número \033[4;36m{}\033[m. \nTente novamente!".format(compiuter, jogador))
