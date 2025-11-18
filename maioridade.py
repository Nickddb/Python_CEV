print("MAIORIDADE")
from datetime import date
atual = date.today().year
soma = 0
soma2 = 0


for m in range(0,3):
    ano = int(input(f"Digite o ano de nascimento da {m+1}ª pessoa: "))
    idade = atual - ano
for a in range(0,3):
    if idade >= 18:
        soma = soma + 1
        print(soma, " pessoas atingiram a maioridade.")
    else:
        soma2 = soma2 + 1
        print(soma2, " pessoas não atingiram a maioridade.")
