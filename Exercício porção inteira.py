from math import trunc
num = float(input('Por favor, digite um número para que eu mostre a sua porção inteira '))
porção = trunc(num)
print('A porção inteira do número \033[1;30;44m', num, '\033[m é: \033[1;34m',porção)
