nome = str(input('Digite um nome completo: ')).strip()
print('O nome em letras maiúsculas fica {}'.format(nome.upper()))
print('O nome em letras minúsculas fica {}'.format(nome.lower()))
print('Ao todo o nome {} tem {} letras'.format(nome, len(nome) - nome.count(' '))) #Sem espaços
print('O primeiro nome tem {} letras'.format(nome.find(' ')))