from random import shuffle, choice
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
chamada = [a1, a2, a3, a4]
sorteado = choice(chamada)
print('O sorteado para limpar a lousa foi {}'.format(sorteado))
shuffle(chamada)
print('E a ordem de apresentação será:')
print(chamada)
