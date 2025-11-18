print("\033[41mPROGRESSÃO ARITMÉTICA\033[m")

primeiro = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
an = primeiro + (10 - 1) * razao

print("Lista dos 10 primeiros termos: ")
for pa in range(primeiro, an + razao, razao):
    print('{} '.format(pa), end='-> ')
print("END")