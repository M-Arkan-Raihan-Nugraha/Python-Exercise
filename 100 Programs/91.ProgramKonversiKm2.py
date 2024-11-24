# DIBUAT OLEH: M ARKAN RAIHAN NUGRAHA
# TANGGAL DIBUAT: 10 NOVEMBER 2024
# PROGRAM MENGKONVERSI LUAS KILOMETER PERSEGI KE METER PERSEGI, HEKTAR, KAKI PERSEGI, DAN ACRE

print('='*25)
print('PROGRAM KONVERSI KM2')
print('='*25)

km2 = float(input('Masukkan Luas Kilometer Persegi: '))
m2 = km2 * 1000000
ha = km2 * 100
ft2 = km2 * 10763910.4
acre = km2 * 247.105

print('Hasil Konversi:')
print(m2, 'Meter Persegi')
print(ha, 'Hektar')
print(ft2, 'Kaki Persegi')
print(acre, 'Acre')