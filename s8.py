print('''
========================
PROGRAM TABUNG
========================
''')

r = float(input('Masukan Jari-jari: '))
t = float(input('Masukan Tinggi: '))
v = 2 * 3.14 * r * t
lp = 3.14 * r * r + 2 * 3.14 * r * t

print('Volume:' , v , 'cm3')
print('Luas Permukaan:' , lp , 'cm2')