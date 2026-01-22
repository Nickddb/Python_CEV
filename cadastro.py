print("\033[3;35mCADASTRO DE PESSOAS\033[m")
cont = age = masculino = mulher = 0
while True:
    cont += 1
    idade = int(input(f"Digite a idade da {cont}ª pessoa: "))
    sex = str(input("Digite o sexo da mesma pessoa [F/M]: ")).strip().upper()[0]
    if idade >= 18:
        age+=1
    if sex == 'M':
        masculino+=1
    if sex == 'F' and idade <= 19:
        mulher+=1
    continuar = str(input("\nDeseja continuar cadastrando mais pessoas? ")).strip().upper()[0]
    if continuar == 'N':
        break
print("\033[1m=\033[m"*30)
print(f"Ao total,", end=' ')
if age >= 2:
    print(f"\033[1;34m{age}\033[m pessoas maiores de idade foram cadastradas;", end=' ')
elif age == 1:
    print(f"\033[1;34m{age}\033[m pessoa maior de idade foi cadastrada;", end=' ')
else:
    print(f"\033[1;34mNenhuma\033[m pessoa maior de idade foi cadastrada;", end=' ')
if masculino >= 2:
    print(f"\033[1;32m{masculino}\033[m homens foram cadastrados e ")
elif masculino == 1:
    print(f"\033[1;32m{masculino}\033[m homem foi cadastrado e ")
else:
    print(f"\033[1;32mNenhum\033[m homem foi cadastrado e ")
if mulher >= 2:
    print(f"\033[1;37m{mulher}\033[m mulheres com menos de 20 anos foram cadastradas")
elif mulher == 1:
    print(f"\033[1;37m{mulher}\033[m mulher com menos de 20 anos foi cadastrada")
else:
    print(f"\033[1;37mNenhuma\033[m mulher com menos de 20 anos foi cadastrada")
