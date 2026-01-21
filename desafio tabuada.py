num = 1
print("\033[3;32mTABUADA || Safeword: Qualquer número negativo\033[m")
while num >= 0:
    num = int(input('Digite um número: '))
    if num >= 0:
        for t in range( 0, 11):
            print('{} X {:2} = \033[1;34m{}\033[m'.format(num, t, num * t))
        print("=" * 10)
    else:
        print("Tabuada encerrada")
        break