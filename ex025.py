#Crie um programa qque leia o nome de uma pessoa e diga se ela tem "Silva" no nome.
nome = str(input('Qual o seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))
