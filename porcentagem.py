si = float(input('O seu salário atual irá receber 15% de aumento. Qual o seu salário atual?: '))
s = (si * 15) /100
sf = si + s
print('O seu novo salário será de \033[1;35mR$', sf, "\033[m")
print("=" * 20)
d = float(input('Digite o valor do preço de um bis a seguir: '))
b = (d * 5) / 100
bf = d - b
print('O seu valor, com 5% de desconto é de', bf)

