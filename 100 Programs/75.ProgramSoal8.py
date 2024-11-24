# DIBUAT OLEH: M ARKAN RAIHAN NUGRAHA
# TANGGAL DIBUAT: 08 NOVEMBER 2024
# PROGRAM MENGHITUNG VOLUME DAN LUAS PERMUKAAN TABUNG

print('='*20)
print('PROGRAM SOAL 8')
print('='*20)
print('''
========================
PROGRAM TABUNG
========================
''')

r = float(input('Masukkan Jari-jari: '))
t = float(input('Masukkan Tinggi: '))
v = 2 * 3.14 * r * t
lp = 3.14 * r * r + 2 * 3.14 * r * t

print('Volume:' , v , 'cm3')
print('Luas Permukaan:' , lp , 'cm2')