r = float(input('Observe este retângulo, que você irá pintar de branco, |___|. Você sabe o quanto de tinta irá precisar para pintá-lo? Não? Bem, primeiramente, quantos metros ele tem de largura? '))
r2 = float(input('E de altura? '))
a = r * r2
l = (r * r2) // 2
print('Ótimo! A sua área é de', a, 'm². E, levando em conta que cada litro de tinta cobre 2m², você irá precisar de', l,'litros de tinta! Boa sorte!')