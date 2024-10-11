# DIBUAT OLEH: M ARKAN RAIHAN NUGRAHA
# TANGGAL DIBUAT: 05 Oktober 2024
# PROGRAM MENGKONVERSI HARI KE TAHUN-BULAN-HARI

print('='*22)
print('PROGRAM KONVERSI HARI')
print('='*22)

HARI_TAHUN = 30 * 12
hari = int(input('Masukan Hari: '))
tahun = int(hari / 365)
hari = hari % HARI_TAHUN
bulan = int(hari / 30)
hari = hari % 30

print('Hasil Konversi: ', tahun, 'tahun', bulan, 'bulan', hari, 'hari')