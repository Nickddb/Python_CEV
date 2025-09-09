from math import radians, sin, cos, tan
an = float(input('Digite um ângulo: '))
seno = sin(radians(an))
print('O ângulo de \033[1;34m{}\033[m tem o \033[1;34mseno \033[m de {:.2f}'.format(an, seno))
cos = cos(radians(an))
print('O ângulo de \033[1;35m{}\033[m tem o \033[1;35mcosseno \033[m de {:.2f}'.format(an, cos ))
tang = tan(radians(an))
print('O ângulo de \033[1;36m{}\033[m tem a \033[1;36mtangente \033[m de {:.2f}'.format(an, tang))
