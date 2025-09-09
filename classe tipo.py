n1 = int(str(input('Digite um valor: ')))
n2 = int(str(input('digite um outro valor: ')))
s = n1 + n2
# print('A soma entre', n1,'e',n2, 'vale',s)
print('A soma entre \033[1;35m{}\033[m e \033[1;36m{}\033[m vale \033[1;34m{}'.format(n1, n2, s))
print(type(n1))
print(type(n2))
