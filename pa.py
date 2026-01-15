print("\033[41mPROGRESSÃO ARITMÉTICA\033[m")
print("\n\033[1;34m============ VERSÃO FOR ============\033[m\n")
primeiro = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
an = primeiro + (10 - 1) * razao

print("\nLista dos 10 primeiros termos: ")
for pa in range(primeiro, an + razao, razao):
    print('{} '.format(pa), end='-> ')
print("END")

print("\n\033[1;34m============ VERSÃO WHILE ============\033[m\n")
print("\033[4mPrimeiro termo: {}; razão: {}\033[m".format(primeiro,razao))
total = 0
termo = 10
p = primeiro
an = 1
while termo != 0:
    total = total + termo
    while an <= total:
        print('{} '.format(p), end='-> ')
        p += razao
        an += 1
    print("END")
    termo = int(input("\nGostaria de ver mais quantos termos? "))
print("Finalizada a opração com  \033[2;33m{}\033[m termos no total.".format(total))