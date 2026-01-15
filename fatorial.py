num = int(input("Digite um número para descobrir seu \033[1;47mfatorial:\033[m "))


print("\033[1;32m============ VERSÃO WHILE ============\033[m\n")
f = 1
while num > 0:
    print("{} ".format(num), end= ' ')
    print('x ' if num > 1 else '= ', end= ' ')
    f *= num
    num -= 1
print("\033[1;35m{}\033[m".format(f))
