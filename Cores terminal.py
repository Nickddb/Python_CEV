print("===== Cor do Texto ==== |", end=" ")
print("==== Estilo do texto ==== |", end=" ")
print("==== Fundo do texto ==== \n")

print("\033[30mCor branca   \033[m", end="           ") #Não funciona, acho que é porque no terminal já é branco
print("         \033[0mEstilo normal", end="              ")
print("\033[40mFundo branco \033[m") #Não funciona, não sei porquê

print("\033[31mCor Vermelha \033[m", end="           ")
print("         \033[1mEstilo negrito\033[m", end="             ")
print("\033[41mFundo Vermelho \033[m")


print("\033[32mCor verde \033[m", end="           ")
print("           \033[4mEstilo sublinhado\033[m", end="           ")
print("\033[42mFundo verde \033[m")


print("\033[33mCor amarela \033[m", end="           ")
print("          \033[7mEstilo negativo\033[m", end="            ")
print("\033[43mFundo amarelo \033[m")


print("\033[34mCor azul \033[m", end="                                                   ")
print("\033[44mFundo azul \033[m")


print("\033[35mCor roxa \033[m", end="                                                   ")
print("\033[45mFundo roxo \033[m")


print("\033[36mCor ciano \033[m", end="                                                  ")
print("\033[46mFundo ciano \033[m")


print("\033[37mCor cinza \033[m", end="                                                  ")
print("\033[47mFundo cinza \033[m")
