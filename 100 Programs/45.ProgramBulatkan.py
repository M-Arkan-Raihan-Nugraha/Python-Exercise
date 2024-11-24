# DIBUAT OLEH: M ARKAN RAIHAN NUGRAHA
# TANGGAL DIBUAT: 26 Oktober 2024
# PROGRAM MEMBULATKAN NILAI BELANJA DENGAN UANG PECAHAN TERENDAH

print('='*20)
print('PROGRAM BULATKAN')
print('='*20)

nb = int(input('Masukkan Nilai Belanja: '))
sisa = nb % 25
hasil = nb - sisa

if sisa != 0:
    print('Total Belanja: ', hasil)
else:
    print('Total Belanja: ', nb)