# DIBUAT OLEH: M ARKAN RAIHAN NUGRAHA
# TANGGAL DIBUAT: 11 OKTOBER 2024
# PROGRAM MENGHITUNG JARAK DUA TANGGAL

print('='*25)
print('PROGRAM JARAK TANGGAL')
print('='*25)

print('Tanggal Pertama (dd:mm:yy)')
tgl1 = int(input('Masukkan Tanggal: '))
bln1 = int(input('Masukkan Bulan: '))
thn1 = int(input('Masukkan Tahun: '))
hari1 = tgl1 + bln1 * 30 + thn1 * 365

print('Tanggal Kedua (dd:mm:yy)')
tgl2 = int(input('Masukkan Tanggal: '))
bln2 = int(input('Masukkan Bulan: '))
thn2 = int(input('Masukkan Tahun: '))
hari2 = tgl2 + bln2 * 30 + thn2 * 365

hari = hari2 - hari1
tahun = hari / 365
hari = hari % 365
bulan = hari / 30
hari = hari % 30

print('Jarak Kedua Tanggal: ', round(tahun), 'Tahun', round(bulan), 'Bulan', round(hari), 'Hari' )