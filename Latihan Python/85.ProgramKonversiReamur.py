# DIBUAT OLEH: M ARKAN RAIHAN NUGRAHA
# TANGGAL DIBUAT: 10 NOVEMBER 2024
# PROGRAM MENGKONVERSI SUHU REAMUR KE CELSIUS, FAHRENHEIT, DAN KELVIN

print('='*25)
print('PROGRAM KONVERSI REAMUR')
print('='*25)

r = float(input('Masukkan Suhu Reamur: '))
c = 5/4 * r
f = 9/4 * r + 32
k = 5/4 * r + 273.15

print('Hasil Konversi:')
print(c, 'Celsius')
print(f, 'Fahrenheit')
print(k, 'Kelvin')