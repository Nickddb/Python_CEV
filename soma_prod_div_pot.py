n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
d1 = n1 // n2
e = n1 ** n2
print('A soma é \033[1;31m{}\033[m, o produto é \033[1;32m{}\033[m e a divisão é \033[1;33m{:.3f}\033[m.'.format(s, m ,d), end=' ')
print('Divisão inteira \033[1;35m{}\033[m e potência \033[1;34m{}\033[m'.format(d1, e))
