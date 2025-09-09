print("\033[mPROGRESSÃO ARITMÉTICA\033[m")

primeiro = float(input("Digite o primeiro termo: "))
razao = float(input("Digite a razão: "))

print("Lista dos 10 primeiros termos: ")
for pa in range(0, 10):
    an = primeiro + (10 - 1) * razao
    print(f"{pa+1}º termo: ", an)