# DIBUAT OLEH: M ARKAN RAIHAN NUGRAHA
# TANGGAL DIBUAT: 10 NOVEMBER 2024
# PROGRAM MENGKONVERSI MASSA OUNCE KE GRAM, KILOGRAM, TON, DAN POUND

print('='*25)
print('PROGRAM KONVERSI OUNCE')
print('='*25)

oz = float(input('Masukkan Massa Ounce: '))
g = oz * 28.3495
kg = oz * 0.0283495
t = oz / 35274
lb = oz / 16

print('Hasil Konversi:')
print(g, 'Gram')
print(kg, 'Kilogram')
print(t, 'Ton')
print(lb, 'Pound')