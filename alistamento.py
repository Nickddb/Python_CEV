print("\033[7mALISTAMENTO MILITAR\033[m")
anon = int(input("Digite o seu ano de nascimento: "))
anoa = int(input("Digite o ano atual: "))

if (anoa - anon) == 18:
    print("\033[1;32mÉ hora de se alistar!\033[m")
elif (anoa - anon) < 18:
    if 18 - (anoa - anon) == 1:
        print("Falta ainda \033[1;33m", 18 - (anoa - anon), "\033[m ano para se alistar!")
    else:
        print("Faltam ainda \033[1;33m", 18 - (anoa - anon), "\033[m anos para se alistar!")
else:
    if (anoa - anon) - 18 == 1:
        print("Já se passou \033[1;31m", (anoa - anon) - 18, " ano\033[m, é preciso se alistar!")
    else:
        print("Já se passaram \033[1;31m", (anoa - anon) - 18, " anos\033[m, é preciso se alistar!")
