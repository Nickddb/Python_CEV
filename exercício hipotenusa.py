from math import hypot
Ca = float(input('Qual o comprimento do cateto adjacente? '))
Co = float(input('E qual o comprimento do cateto oposto? '))
hip = hypot(Co, Ca)
print('A sua hipotenusa é de comprimento', hip)
