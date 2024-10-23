# DIBUAT OLEH: M ARKAN RAIHAN NUGRAHA
# TANGGAL DIBUAT: 05 Oktober 2024
# PROGRAM MENGHITUNG LUAS, KELILING, DAN VOLUME TABUNG

print('='*15)
print('PROGRAM TABUNG')
print('='*15)

r = float(input("Masukkan Jari-Jari: "))
t = float(input('Masukan Tinggi: '))
luas = 2 * 3.14 * r**2
keliling = 2 * 3.14 * r
volume = 3.14 * r**2 * t

print('Keliling\t: ' , keliling, 'Cm')
print('Luas\t\t: ' , luas, 'Cm2')
print('Volume\t\t: ' , volume, 'Cm3')