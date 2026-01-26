print("INSERIR VALORES EM UMA TUPLA")
cont = par = tres = 0
for v in range (0,4):
    tupla = int(input(f"Digite o {v+1}º valor: "))
    tupla += tupla
    if tupla == 9:
        cont+=1
    if tupla % 2 == 0:
        par = tupla
tres = tupla.index(3)
print(f"O número 9 apareceu {cont} vezes")
print(f"A posição do primeiro número 3 é: {tres}")
print(par)