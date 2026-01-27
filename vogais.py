print(f"\033[1;34m{'VOGAIS DAS PALAVRAS':^30}\033[m")

palavras = 'livro', 'lapis', 'caneta', 'borracha', 'apontador'
for p in palavras:
    print(f"\nA palavra \033[4;36m{p.upper()}\033[m contém as vogais: ", end= ' ')
    for vogal in p:
        if vogal.lower() in 'aeiou':
            print(vogal, end= ' ')
