from math import radians, sin, cos, tan
an = float(input('Digite um ângulo: '))
seno = sin(radians(an))
print('O ângulo de {} tem o seno de {:.2f}'.format(an, seno))
cos = cos(radians(an))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(an, cos ))
tang = tan(radians(an))
print('O ângulo de {} tem a tangente de {:.2f}'.format(an, tang))
