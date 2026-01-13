'''Ler o sexo de uma pessoa [M/F], se digitar errado, pedir a digitação correta. A pessoa não vai saber o que é pra digitar?? N tendi'''
print("\033[30;46mVERIFICAR O SEXO DA PESSOA\033[m")
sexo = input(str("Digite o sexo de uma pessoa qualquer: ")).strip().upper()[0]

while sexo != 'M':
    if sexo != 'F':
        print("Errado. Tente novamente.")
        sexo = input(str("Digite o sexo de uma pessoa qualquer: ")).strip().upper()[0]
    elif sexo == 'F':
         break
print("\033[32mCorreto!\033[m")