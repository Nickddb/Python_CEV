#Escreva um programa que leia a velocidade de um carro. se ultrapassar 80km/h = multado
#multa = 7 reais por km rodado

print("CÁLCULO DE (POSSÍVEL) MULTA DE VELOCIDADE\nO LIMITE SÃO 80 KM/H")
velocidade = float(input("Digite a velocidade do carro (km/h): "))

if velocidade <=69:
    print("\033[1;32mPassou de boa!\033[m")
elif 70 <= velocidade <=80:
    print("\033[1;33mQuase levou multa, fica esperto hein!\033[m")
else:
    multa = (velocidade - 80) * 7
    print("=========================")
    print("Você \033[1;31multrapassou ", (velocidade - 80) , "Kms\033[m acima do limite, sua multa será de \033[1;34mR$", multa)