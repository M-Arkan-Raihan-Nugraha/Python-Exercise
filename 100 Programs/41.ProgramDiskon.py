# DIBUAT OLEH: M ARKAN RAIHAN NUGRAHA
# TANGGAL DIBUAT: 26 Oktober 2024
# PROGRAM MENGHITUNG DISKON 5% JIKA TOTAL BELANJA LEBIH DARI 100K

print('='* 20)
print('PROGRAM DISKON')
print('='*20)

total = float(input('Masukkan Total Belanja: '))
diskon = total * 5/100
hasil_diskon = total - diskon

if total > 100000:
    print('Diskon: ', diskon)
    print('Total Bayar: ', hasil_diskon)
else:
    print('Anda Tidak Dapat Diskon')
    print('Total Bayar: ', total)