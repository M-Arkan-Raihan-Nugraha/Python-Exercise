# DIBUAT OLEH: M ARKAN RAIHAN NUGRAHA
# TANGGAL DIBUAT: 10 NOVEMBER 2024
# PROGRAM MENGKONVERSI MASSA TON KE GRAM, KILOGRAM, POUND, DAN OUNCE

print('='*25)
print('PROGRAM KONVERSI TON')
print('='*25)

t = float(input('Masukkan Massa Ton: '))
g = t * 1000000
kg = t * 1000
lb = t * 2204.62
oz = t * 35274

print('Hasil Konversi:')
print(g, 'Gram')
print(kg, 'Kilogram')
print(lb, 'Pound')
print(oz, 'Ounce')