''' Aprovar o emprestimo bancario. Ele vai pedir o valor da casa, o salário do comprador
 e em quantos anos ele irá pagar. Calcular valor da prestação mensal,
 sendo que ela não pode exceder 30% do salário ou então o emprestimo será negado.'''

print("EMPRÉSTIMO BANCÁRIO")
casa = float(input("Digite o valor da casa: R$"))
salario = float(input("Digite o valor do salário: R$"))
anos = float(input("Digite o tempo (em anos) em que se pretende pagar: "))
porcentagem = salario * 0.3
prestacao = casa / ( anos * 12)
if prestacao > porcentagem:
    print("\033[1;31mNão pode ser aprovado!\033[m, pois a prestação será de {}, e a porcentagem de 30% equivale a R${} do seu salário" .format(prestacao,porcentagem))
else:
    print("\033[1;32mPode ser aprovado!\033[m, pois a prestação será de {}, e a porcentagem de 30% equivale a R${} do seu salário" .format(prestacao,porcentagem))
