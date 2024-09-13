print('''
\033[91m
===========================
KALOR JENIS ES
===========================
''')

m = float(input('Masukan Massa:'))
c = float(input('Masukan Kalor Jenis Zat:'))
dt = float(input('Masukan Perubahan Suhu:'))
q1 = m * c * dt

print('\033[93m\033[01mKalor Jenis Es:', round(q1))