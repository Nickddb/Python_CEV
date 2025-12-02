print("ANÁLISE")

somaidade = 0
media = 0
idadehomem = 0
nomevelho = ''
totmulher = 0
for a in range(0,3):
    nome = str(input(f"Insira o nome da {a+1}ª pessoa: ")).strip()
    idade = (int(input("Insira a idade dela: ")))
    sexo = str(input("Insira o seu sexo [M/F] : ")).strip()
    print("--" * 12)
    somaidade += idade
    if a == 1 and sexo == 'Mn':
        idadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > idadehomem:
        idadehomem = idade
        nomevelho = nome
    if sexo in 'fF' and idade < 20:
        totmulher += 1


media  = idade / 3
print("A média das idades é igual a {} anos".format(media))
print("O homem mais velho possui {} anos e se chama {}.".format(idadehomem, nomevelho))
print("Ao todo são {} mulheres com menos de 20 anos.".format(totmulher))


