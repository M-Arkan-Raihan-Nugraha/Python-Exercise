print('''
\033[31m
=======================================================
Andi Belanja Buku Dan Alat Tulis Di Suatu Toko Buku.
Toko Buku Tersebut Sedang Promosi Diskon Sebesar 12,5 %
=======================================================
''')

b = float(input('Masukan Harga Buku: '))
at = float(input('Masukan Harga Alat Tulis: '))
total = b + at
diskon = total * 12.5/100
hasil_diskon = total - diskon

print('Total Belanja:', total)
print('Diskon:', diskon)
print('Total Bayar:', hasil_diskon)