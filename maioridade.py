print("MAIORIDADE")
from datetime import date
atual = date.today().year
maior = 0
menor = 0

for m in range(0,3):
    ano = int(input(f"Digite o ano de nascimento da {m+1}ª pessoa: "))
    idade = atual - ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1

if maior == 1:
    print("1 pessoa atingiu a maioridade.")
if maior > 1:
    print(maior, "pessoas atingiram a maioridade.")
else:
   print("Ninguém atingiu a maioridade.")

if menor == 1:
    print(" 1 pessoa não atingiu a maioridade.")
if menor > 1:
    print(menor, "pessoas não atingiram a maioridade.")
else: 
    print("Ninguém faltou atingir a maioridade")
