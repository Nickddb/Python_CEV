nota1 = float(input('Qual a sua primeira nota? '))
nota2 = float(input('Qual a sua segunda nota? '))
m = (nota1 + nota2) / 2
print('A sua média é de: \033[1;33m', m)

print("IF Simples")
n1 = float(input("Digite a 1ª nota: "))
n2 = float(input("Digite a 2ª nota: "))
media = (n1 + n2) / 2
print("A sua média foi {:.1f}".format(media))
if media >= 7:
    print("\033[1;32mBoa!!\033[m")
else:
    print("\033[1;36mBora estudar, que a vida não é um morango?\033[m")

print("---------------------")
print("IF Simplificado")
n1 = float(input("Digite a 1ª nota: "))
n2 = float(input("Digite a 2ª nota: "))
media = (n1 + n2) / 2
print("\033[1;32mBoa!!\033[m" if media >=7 else "\033[1;36mBora estudar, que a vida não é um morango?\033[m")
