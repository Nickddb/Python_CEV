print("\033[mLER 6 NÚMEROS INTEIROS\033[m")
soma = 0
cont = 0
for i in range(0, 6):
    num = int(input(f"Digite o  {i+1}º  número: "))
    if num % 2 == 0:
        soma += num
        cont += 1
if cont == 0:
    print("Não foram encontrados nenhum número par")
else:
    print("Foram informados", cont, " números e a soma é igual a: ", soma)
