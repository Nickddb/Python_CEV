print("\033[7m NÚMERO PRIMO\033[m")
num = int(input("Digite um número: "))
tot = 0

for p in range(1, num + 1):
    if num % p == 0:
        print("\033[32m", end='')
        tot += 1
    else:
        print("\033[31m", end='')
    print('{} '.format(p), end='')
print("\n\033[mO número {} foi divisível {} vezes".format(num, tot))

if tot == 2:
    print("Por isso ele é primo!")
else:
    print("Por isso ele NÃO é primo!")
