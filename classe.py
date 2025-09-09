Thing = input('Digite algo: ')
print('O tipo primitivo disso é \033[46m',(type(Thing), (Thing.isnumeric()), (Thing.isalpha()), (Thing.isupper())), "\033[m")
