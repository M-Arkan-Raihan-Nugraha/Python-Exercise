# DIBUAT OLEH: M ARKAN RAIHAN NUGRAHA
# TANGGAL DIBUAT: 10 NOVEMBER 2024
# PROGRAM MENGKONVERSI LUAS METER PERSEGI KE KILOMETER PERSEGI, HEKTAR, KAKI PERSEGI, DAN ACRE

print('='*20)
print('PROGRAM KONVERSI M2')
print('='*20)

m2 = float(input('Masukkan Luas Meter Persegi: '))
km2 = m2 / 1000000
ha = m2 / 10000
ft2 = m2 * 10.7639
acre = m2 / 4046.86

print('Hasil Konversi:')
print(km2, 'Kilometer Persegi')
print(ha, 'Hektar')
print(ft2, 'Kaki Persegi')
print(acre, 'Acre')