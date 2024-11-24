# DIBUAT OLEH: M ARKAN RAIHAN NUGRAHA
# TANGGAL DIBUAT: 10 NOVEMBER 2024
# PROGRAM MENGKONVERSI LUAS HEKTAR KE METER PERSEGI, KILOMETER PERSEGI, KAKI PERSEGI, DAN ACRE

print('='*20)
print('PROGRAM KONVERSI HA')
print('='*20)

ha = float(input('Masukkan Luas Hektar: '))
m2 = ha * 10000
km2 = ha / 100
ft2 = ha * 107639
acre = ha * 2.47105

print('Hasil Konversi:')
print(m2, 'Meter Persegi')
print(km2, 'Kilometer Persegi')
print(ft2, 'Kaki Persegi')
print(acre, 'Acre')