nome = str(input('Qual o seu nome?: '))
if nome == 'Gustavo':
    print("\033[1;43mQue nome lindo!\033[m")
else:
      print("Seu nome é \033[1;45mnormal.\033[m")
print("Bom dia, {}!".format(nome))
