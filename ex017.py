#import math ou abixo para selecionar só hipotenusa 
from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
h = hypot(co, ca)

print('A hipotenusa vai medir {:.2f}'.format(h))