num = int(input("Digite um número até 9999: "))
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10
print('=' * 12)
print("\033[1;44mUnidade: ", unidade, "\033[m")
print("\033[1;45mDezena: ", dezena, "\033[m")
print("\033[1;46mCentena: ", centena, "\033[m")
print("\033[1;47mMilhar: ", milhar, "\033[m")
print('=' * 12)
