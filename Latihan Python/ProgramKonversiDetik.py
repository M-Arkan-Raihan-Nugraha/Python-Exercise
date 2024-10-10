# DIBUAT OLEH: M ARKAN RAIHAN NUGRAHA
# TANGGAL DIBUAT: 08 Oktober 2024
# PROGRAM MENGKONVERSI DETIK KE HARI, JAM, MENIT, DAN DETIK

print('='*25)
print('PROGRAM KONVERSI DETIK')
print('='*25)

DETIK_HARI = 60 * 60 * 24
DETIK_JAM = 60 * 60
detik = int(input('Masukan Detik: '))
hari = int(detik / DETIK_HARI)
detik = detik % DETIK_HARI
jam = int(detik / DETIK_JAM)
detik = detik % DETIK_JAM
menit = int(detik / 60)
detik = detik % 60

print('Hasil Konversi: ', hari, 'hari', jam, 'jam', menit, 'menit', 'dan', detik, 'detik')