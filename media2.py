print("\033[7mCALCULAR MÉDIA\033[m")
nota1 = float(input("Entre com a 1ª nota: "))
nota2 = float(input("Entre com a 2ª nota: "))
media = (nota1 + nota2) / 2

if media < 5:
    print("\033[1;31mREPROVADA!\033[m \033[37m(voz do Seu Madruga)\033[m")
    print("Média igual a ", media)
elif media >= 5 and media < 6.9:
    print("\033[1;32mRecuperação!\033[m")
    print("Média igual a ", media)
else:
    print("\033[1;32mAPROVADO!\033[m")
    print("Média igual a ", media)

