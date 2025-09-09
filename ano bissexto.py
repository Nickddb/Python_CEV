#Faça um programa que leia um ano qualquer e diga se é bissexto
from datetime import date
print("ANO BISSEXTO")
ano = int(input("Digite um ano para descobrir se ele é bissexto ou digite 0 para usar o ano atual: "))

print("IF SIMPLES")
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano é \033[1;33mbissexto!\033[m")
else:
    print("O ano \033[1;31mnão\033[m é bissexto.")

print("\nIF SIMPLIFICADO")
print("O ano é \033[1;33mbissexto!\033[m" if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 else "O ano \033[1;31mnão\033[m é bissexto")