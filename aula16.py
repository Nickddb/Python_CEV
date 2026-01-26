lanche = 'Hamburguer', 'suco', 'pizza', 'pudim'
print(lanche[1][3])
for cont in range(0, len(lanche)):
    print(lanche[cont] ,cont)
print("="*20)
for pos, comida in enumerate(lanche):
    print(comida, pos)