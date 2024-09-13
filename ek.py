print('''
\033[92m
===========================
ENERGI KINETIK
===========================
''')

m = float(input('Masukan Massa:'))
v = float(input('Masukan kecepatan Benda:'))
ek = 1/2 * m * v * v

print('\033[94m\033[01mEnergi Kinetik:', round(ek))