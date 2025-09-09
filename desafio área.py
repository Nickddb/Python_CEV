r = float(input('Observe este retângulo, que você irá pintar de branco, |___|. \nVocê sabe o quanto de tinta irá precisar para pintá-lo? Não? Bem, primeiramente, quantos metros ele tem de largura? '))
r2 = float(input('E de altura? '))
a = r * r2
l = (r * r2) // 2
print('Ótimo! A sua \033[1;41márea\033[m é de \033[1;41m', a, 'm².\033[m E, levando em conta que cada litro de tinta cobre 2m², você irá precisar de \033[1;34m', l,'\033[mlitros de tinta! Boa sorte!')