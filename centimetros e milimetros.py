m = bool(input('Digite um valor '))
cm = m / 0.001
mm = m / 0.0001
print('Seu valor em \033[1;33mcentímetros\033[m é \033[1;33m{}\033[m e em \033[1;36mmilímetros\033[m é \033[1;36m{}\033[m' .format(cm, mm))
