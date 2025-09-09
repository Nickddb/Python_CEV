print(f'{"\033[7mCONDIÇÕES DE PAGAMENTO\033[m":^45}')

valor = float(input("Digite o preço:  R$"))
print("1- À vista dinheiro/cheque: 10% de desconto;\n2- À vista no cartão: 5% de desconto;\n3- Em até 2x no cartão: preço normal;\n4- 3x ou mais no cartão: 20% de juros;")
condicao = int(input("Escolha um método: "))

if condicao == 1:
    desconto = valor - (valor * 0.1)
    print("O novo preço será de \033[1;34mR${}\033[m, com R$".format(desconto), (valor * 0.1), " de desconto")
elif condicao == 2:
    desconto = valor - (valor * 0.05)
    print("O novo preço será de \033[1;34mR${}\033[m, com R$".format(desconto), (valor * 0.05), " de desconto")
elif condicao == 3:
    print("\033[1;34mO preço continuará o mesmo.\033[m")
elif condicao > 4:
    print("\033[1;31mOpcção errada.\033[m")
else:
    desconto = valor + (valor * 0.2)
    parcela = int(input("Quantas parcelas? "))
    parcela = desconto / parcela
    print("O novo preço será de R${}, com R$".format(desconto), (valor * 0.2), " de juros e com parcelas de valor unitário de R${:.2f}".format(parcela))