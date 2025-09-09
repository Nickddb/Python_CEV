'''Ler um número inteiro e pedir pro usuário escolher qual a base de conversão: 1- binário; 2- octal; 3- hexadecimal'''

print("\033[7mBASE DE CONVERSÃO\033[m")
num = int(input("Digite um número para converter: "))
opcao = int(input("TABELA:\n\033[1;46m1 - Binário;\033[m\n\033[1;45m2 - Octal;\033[m\n\033[1;47m3 - Hexadecimal;\033[m\n"))

if opcao == 1:
    print("Binário: \033[1;32m",bin(num)[2:], "\033[m")
elif opcao == 2:
    print("Octal: \033[1;32m", oct(num)[2:], "\033[m")
elif opcao == 3:
    print("Hexadecimal: \033[1;32m", hex(num)[2:], "\033[m")
else:
    print("\033[1;31mOpção errônea!\033[m")

