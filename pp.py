# Percepatan Rata rata 
# a= v2-v1/ t2 - t1

print('''
\033[92m
===========================
PERCEPATAN RATA-RATA
===========================
''')

v1 = float(input('Masukan kecepatan 1:'))
v2 = float(input('Masukan kecepatan 2:'))
t1 = float(input('Masukan waktu 1:'))
t2 = float(input('Masukan waktu 2:'))
a = v2 - v1 / t2 - t1

print('\033[94m\033[01mPERCEPATAN RATA-RATA:', round(a))