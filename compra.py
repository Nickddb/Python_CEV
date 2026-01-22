print("\033[2;42mCOMPRA\033[m")
cont = prod = menor = soma = 0
barato = ' '
continuar = 'S'
while continuar == 'S':
    cont+=1
    nome_prod = str(input(f"Digite o nome do {cont}º produto: "))
    preco_prod = float(input("E o seu preço: "))
    soma += preco_prod
    if preco_prod >= 1000:
        prod+=1
    if cont == 1 or preco_prod < menor:
        menor = preco_prod
        barato = nome_prod
    resp = ' '
    if preco_prod < preco_prod:
        print(nome_prod)
    continuar = str(input("\nContinuar registrando produtos? ")).strip().upper()[0]
print("="*20)
print(f"\033[2;34mTotal gasto: R${soma}\033[m")
print(f"\033[1;43m{prod}\033[m produtos custam mais de R$1000 e \033[1;41m{barato}\033[m é o produto mais barato, custando R${menor}")