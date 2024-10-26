# DIBUAT OLEH: M ARKAN RAIHAN NUGRAHA
# TANGGAL DIBUAT: 05 Oktober 2024
# PROGRAM MENGHITUNG LUAS PERMUKAAN, KELILING, DAN VOLUME KERUCUT

print('='*15)
print('PROGRAM KERUCUT')
print('='*15)

r = float(input("Masukkan Jari-Jari: "))
t = float(input('Masukan Tinggi: '))
s = float(input('Masukan Garis Pelukis: '))
luas = 3.14 * r * (r + s)
keliling = 2 * 3.14 * r
volume = 1/3 * 3.14 * r**2 * t

print('Keliling\t: ' , keliling, 'Cm')
print('Luas Permukaan\t: ' , luas, 'Cm2')
print('Volume\t\t: ' , volume, 'Cm3')