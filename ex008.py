medida = float(input(('Uma distância em metros ')))
cm = medida * 100
mm = medida * 1000
km = medida / 1000
print('A medida de {}m corresponde a:'.format(medida))
print('{:.1f}km'.format(km))
print('{:.0f}cm'.format(cm))
print('{:.0f}mm'.format(mm))