#acabar o loop while quando a pessoa não quiser ver mais nenhum termo adicional
print("\033[41mPROGRESSÃO ARITMÉTICA\033[m")
print("============ VERSÃO FOR ============\n")
primeiro = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
an = primeiro + (10 - 1) * razao

print("Lista dos 10 primeiros termos: ")
for pa in range(primeiro, an + razao, razao):
    print('{} '.format(pa), end='-> ')
print("END")


print("============ VERSÃO WHILE ============\n")