# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')

#.strip retirou os espaços e o upper jogou tudo pra maiúsculo pra não ter diferenciação.
# [] limitou os caracteres