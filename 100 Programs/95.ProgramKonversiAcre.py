# DIBUAT OLEH: M ARKAN RAIHAN NUGRAHA
# TANGGAL DIBUAT: 10 NOVEMBER 2024
# PROGRAM MENGKONVERSI LUAS ACRE KE METER PERSEGI, KILOMETER PERSEGI, HEKTAR, DAN KAKI PERSEGI

print('='*25)
print('PROGRAM KONVERSI Acre')
print('='*25)

acre = float(input('Masukkan Luas Acre: '))
m2 = acre * 4046.86
km2 = acre / 247.105
ha = acre * 0.404686
ft2 = acre * 43560

print('Hasil Konversi:')
print(m2, 'Meter Persegi')
print(km2, 'Kilometer Persegi')
print(ha, 'Hektar')
print(ft2, 'Kaki Persegi')