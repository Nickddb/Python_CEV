num = int(input('Digite um número: '))

for t in range( 0, 11):
    print('{} X {:2} = \033[1;34m{}\033[m'.format(num, t, num * t))