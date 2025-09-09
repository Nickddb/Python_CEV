from math import hypot
Ca = float(input('Qual o comprimento do \033[4;45mcateto adjacente?\033[m '))
Co = float(input('E qual o comprimento do \033[4;46mcateto oposto?\033[m '))
hip = hypot(Co, Ca)
print('A sua \033[4;44mhipotenusa\033[m é de comprimento \033[1;34m', hip)
