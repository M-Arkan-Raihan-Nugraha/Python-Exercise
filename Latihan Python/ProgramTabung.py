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

print('Keliling\t: ' , round(keliling,2) , 'Cm')
print('Luas\t\t: ' , round(luas,2) , 'Cm2')
print('Volume\t\t: ' , round(volume,2) , 'Cm3')