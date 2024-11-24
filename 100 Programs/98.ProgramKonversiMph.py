# DIBUAT OLEH: M ARKAN RAIHAN NUGRAHA
# TANGGAL DIBUAT: 10 NOVEMBER 2024
# PROGRAM MENGKONVERSI KECEPATAN MIL PER JAM KE METER PER DETIK, KILOMETER PER JAM, KAKI PER DETIK, DAN KNOT

print('='*25)
print('PROGRAM KONVERSI MPH')
print('='*25)

mph = float(input('Masukkan Kecepatan Mil Per Jam: '))
ms = mph / 2.23694
kmj = mph * 1.60934
fts = mph * 1.46667
kt = mph * 0.868976

print('Hasil Konversi:')
print(ms, 'm/s')
print(kmj, 'km/jam')
print(fts, 'ft/s')
print(kt, 'kt')