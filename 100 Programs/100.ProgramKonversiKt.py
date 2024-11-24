# DIBUAT OLEH: M ARKAN RAIHAN NUGRAHA
# TANGGAL DIBUAT: 10 NOVEMBER 2024
# PROGRAM MENGKONVERSI KECEPATAN KNOT KE METER PER DETIK, KILOMETER PER JAM, MIL PER JAM, DAN KAKI PER DETIK

print('='*25)
print('PROGRAM KONVERSI KNOT')
print('='*25)

kt = float(input('Masukkan Kecepatan Knot: '))
ms = kt * 0.514444
kmj = kt * 1.852
mph = kt * 1.15078
fts = kt * 1.68781

print('Hasil Konversi:')
print(ms, 'm/s')
print(kmj, 'km/jam')
print(mph, 'mph')
print(fts, 'ft/s')