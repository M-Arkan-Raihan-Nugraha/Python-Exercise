# DIBUAT OLEH: M ARKAN RAIHAN NUGRAHA
# TANGGAL DIBUAT: 10 NOVEMBER 2024
# PROGRAM MENGKONVERSI SUHU FAHRENHEIT KE CELSIUS, KELVIN, DAN REAMUR

print('='*30)
print('PROGRAM KONVERSI FAHRENHEIT')
print('='*30)

f = float(input('Masukkan Suhu Fahrenheit: '))
c = 5/9 * (f-32)
k = 5/9 * (f-32) + 273.15
r = 4/9 * (f-32)

print('Hasil Konversi:')
print(c, 'Celsius')
print(k, 'Kelvin')
print(r, 'Reamur')