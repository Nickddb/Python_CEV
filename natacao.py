from datetime import date
print("\033[7mCATEGORIA DE NATAÇÃO!\033[m")
ano = date.today().year

nascimento = int(input("Digite o ano de nascimento: "))
idade = ano - nascimento
if idade <= 9:
    print("\033[1;31mMirim\033[m")
elif idade <= 14:
    print("\033[1;32mInfantil\033[m")
elif idade <= 19:
    print("\033[1;33mJúnior\033[m")
elif idade <= 25:
    print("\033[1;34mSênior\033[m")
else:
    print("\033[1;35mMaster\033[m")