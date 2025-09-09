from time import sleep

print("\033[7mCONTAGEM REGRESSIVA\033[m")
'''10, -1 (para pegar o 0, precisa colocar isso, senão para no 1), -1 (vai diminuir, sem isso, não funciona)'''
for c in range(10, -1, -1):
    print(c)
    sleep(0.5)
print("\033[1;34mFELIZ ANO NOVO!\033[m")