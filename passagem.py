#Faça um programa que pergunte a distância de uma viagem em km. Calcular o preço da passagem (50 centavos)
#p/ viagens de até 200km e 45 centavos p/ viagens mais longas

print("CALCULAR A PASSAGEM")
km = float(input("Digite quantos km de distância entre o local de saída e o local de chegada: "))

if km <= 200:
    passagem = km * 0.5
    print("O valor da sua passagem será de \033[1;32mR$",passagem)
else:
    passagem = km * 0.45
    print("O valor da sua passagem será de \033[1;33mR$",passagem)
