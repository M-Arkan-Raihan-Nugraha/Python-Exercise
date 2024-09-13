print('''
\033[91m
===========================
KALOR JENIS AIR
===========================
''')

m = float(input('Masukan Massa:'))
cAir = float(input('Masukan Kalor Jenis Zat Air:'))
dt = float(input('Masukan Perubahan Suhu:'))
q3 = m * cAir * dt

print('\033[93m\033[01mKalor Jenis Air:', round(q3))