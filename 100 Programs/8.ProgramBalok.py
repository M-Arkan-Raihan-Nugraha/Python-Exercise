# DIBUAT OLEH: M ARKAN RAIHAN NUGRAHA
# TANGGAL DIBUAT: 05 Oktober 2024
# PROGRAM MENGHITUNG LUAS PERMUKAAN, KELILING, DAN VOLUME BALOK

print('='*15)
print('PROGRAM BALOK')
print('='*15)

p = float(input("Masukkan Panjang: "))
l = float(input('Masukan Lebar: '))
t = float(input('Masukan Tinggi: '))
luas = 2 * (p*l + p*t + l*t)
keliling = p * l * t
volume = 4 * (p+l+t)

print('Keliling\t: ' , keliling, 'Cm')
print('Luas Permukaan\t: ' , luas, 'Cm2')
print('Volume\t\t: ' , volume, 'Cm3')