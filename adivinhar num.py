from random import randint
compiuter = randint(0,10)
print("\033[42mJOGUINHO DE ADIVINHAÇÃO\033[m \nAdivinhe um número entre \033[1;34m0\033[m e \033[1;34m10\033[m")

contador = 0
acerto = False

while not acerto:
    jogador = int(input("O computador pensou em um número. Digite qual número ele pensou: "))
    contador += 1
    if jogador == compiuter:
        print("\033[1;32mParabéns! Você acertou!\033[m")
        print("Quantidade de palpites: ", contador)
        break
    elif jogador > 10 or jogador < 0:
        print("\033[7mEu falei pra escolher um número entre 0 e 10 apenas!\033[m")
        jogador = int(input("\nO computador pensou em um número. Digite qual número ele pensou: "))
    else:
        if jogador < compiuter:
            print("\033[1;32mMais...\033[m tente novamente")
        elif jogador > compiuter:
            print("\033[1;31mMenos...\033[m tente novamente")
