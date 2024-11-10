# DIBUAT OLEH: M ARKAN RAIHAN NUGRAHA
# TANGGAL DIBUAT: 10 NOVEMBER 2024
# PROGRAM MENGKONVERSI LUAS KAKI PERSEGI KE METER PERSEGI, KILOMETER PERSEGI, HEKTAR, DAN ACRE

print('='*20)
print('PROGRAM KONVERSI FT2')
print('='*20)

ft2 = float(input('Masukkan Luas Kaki Persegi: '))
m2 = ft2 / 10.7639
km2 = ft2 / 10763910.4
ha = ft2 / 107639
acre = ft2 / 43560

print('Hasil Konversi:')
print(m2, 'Meter Persegi')
print(km2, 'Kilometer Persegi')
print(ha, 'Hektar')
print(acre, 'Acre')