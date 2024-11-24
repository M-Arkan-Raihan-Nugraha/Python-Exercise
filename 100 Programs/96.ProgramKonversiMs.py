# DIBUAT OLEH: M ARKAN RAIHAN NUGRAHA
# TANGGAL DIBUAT: 10 NOVEMBER 2024
# PROGRAM MENGKONVERSI KECEPATAN METER PER DETIK KE KILOMETER PER JAM, MIL PER JAM, KAKI PER DETIK, DAN KNOT

print('='*25)
print('PROGRAM KONVERSI M/S')
print('='*25)

ms = float(input('Masukkan Kecepatan Meter Per Detik: '))
kmj = ms * 3.6
mph = ms * 2.23694
fts = ms * 3.28084
kt = ms * 1.94384

print('Hasil Konversi:')
print(kmj, 'km/jam')
print(mph, 'mph')
print(fts, 'ft/s')
print(kt, 'kt')