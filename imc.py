print("\033[7mIMC (ÍNDICE DE MASSA CORPORAL)\033[m")

peso = float(input("Digite o seu peso, em Kg: "))
altura = float(input("Digite a sua altura, em metros: "))
if altura.is_integer():
    altura = altura / 100
imc = peso / (altura * altura)

if imc < 18.5:
    print("Você está abaixo do peso, com IMC igual a {:.2f}kg/m²".format(imc))
elif imc >= 18.5 and imc < 25:
    print("Você está com o peso ideal, com IMC igual a {:.2f}kg/m²".format(imc))
elif imc >= 25 and imc < 30:
    print("Você está acima do peso, com IMC igual a {:.2f}kg/m²".format(imc))
else:
    print("Você está com obesidade mórbida, com IMC igual a {:.2f}kg/m²".format(imc))