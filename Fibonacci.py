print("\033[2;43mSEQUÊNCIA DE FIBONACCI\033[m")
num = int(input("Digite uma quantidade para descobrir a sequência de termos: "))

t1 = 0
t2 = 1
if num == 1:
    print('\033[7m',t1, " -> ", end='FIM ')
elif num == 2:
    print('\033[7m',t1, " -> ", t2, " -> ", end=' FIM')
else:
    print('\033[7m',t1, " -> ", t2, end=' ')
    cont = 3
    while cont <= num:
        t3 = t1 + t2
        print(" -> ", t3, end=' ')
        t1 = t2
        t2 = t3
        cont += 1
    print("-> FIM\033[m")