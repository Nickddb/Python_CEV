frase = str(input("Digite uma frase aleatória: ")).upper().strip()
letra = frase.count('A')
posição1 = frase.split(), frase.find('A')+1
posição2 = frase.split(), frase.rfind('A')+1
print("Quantas vezes aparece a letra 'A': ", letra, "\n\033[1;34mPrimeira", "\033[m", "posição em que aparece: ", posição1, "\n\033[1;32mÚltima", "\033[m", "posição em que aparece: ", posição2)
