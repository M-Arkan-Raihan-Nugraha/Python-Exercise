# DIBUAT OLEH: M ARKAN RAIHAN NUGRAHA
# TANGGAL DIBUAT: 10 NOVEMBER 2024
# PROGRAM MENGKONVERSI KECEPATAN KAKI PER DETIK KE METER PER DETIK, KILOMETER PER JAM, MIL PER JAM, DAN KNOT

print('='*25)
print('PROGRAM KONVERSI FT/S')
print('='*25)

fts = float(input('Masukkan Kecepatan Kaki Per Detik: '))
ms = fts * 0.3048
kmj = fts * 1.09728
mph = fts * 0.681818
kt = fts * 0.592484

print('Hasil Konversi:')
print(ms, 'm/s')
print(kmj, 'km/jam')
print(mph, 'mph')
print(kt, 'kt')