#Programa que leia o comprimento de 3 retas e diga se é possível formarem um triângulo ou não

print("LEI DE EXISTÊNCIA DO TRIÂNGULO")
r1 = float(input("1ª reta: "))
r2 = float(input("2ª reta: "))
r3 = float(input("3ª reta: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Todos os segmentos podem formar triângulo!")
    if r1 != r2 and r1 != r3:
        print("É um triângulo \033[4;35mescaleno!\033[m")
    elif r1 == r2 and r1 != r3:
        print("É um triângulo \033[4;36misósceles!\033[m")
    else:
        print("É um triângulo \033[4;334mequilátero!\033[m")
else:
    print("\033[1;31mNão\033[m pode formar um triângulo!")