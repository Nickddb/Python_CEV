print("PALÍNDROMO")

frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print("Você digitou a frase \033[34m{}\033[m".format(palavras))
if inverso == junto:
    print("O palíndromo de sua frase é igual a: \033[35m", inverso, '\033[m')
else:
    print("E ela \033[31mnão\033[m é um palíndromo!")

