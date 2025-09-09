#Programa que peça o salário e calcule o seu aumento. salários superiores a 1.250 = 10% de aumento
#inferiores ou iguais = 15% de aumento

print("AUMENTO DE SLARIO UHUUUU")
salario = float(input("Digite o seu salário: R$"))

if salario > 1250:
    total = (salario * 0.1) + salario
    print(f"Seu novo salário será igual a \033[1;34mR${total}\033[m")
else:
    total = (salario * 0.15) + salario
    print(f"Seu novo salário será igual a \033[1;35mR${total}\033[m")