print("-" * 40)
print(f"\033[1;46m{'LISTAGEM DE PRODUTOS':^40}\033[m")
print("-" * 40)
prod = 'Pão', 1, 'Algo ali', 2, 'Algo lá', 3
for l in range(0, len(prod)):
    if l % 2 == 0:
        print(f"{prod[l]:.<30}", end= ' ')
    elif l % 2 == 1:
        print(f"R${prod[l]:>7.2f}")
print("-" * 40)