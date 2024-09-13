print('''
\033[31m
============================================
Dapat Diskon 7.5% Kalau Belanja Minimal 200K
============================================
''')

b1 = float(input('Harga Barang 1: '))
b2 = float(input('Harga Barang 2: '))
b3 = float(input('Harga Barang 3: '))
b4 = float(input('Harga Barang 4: '))
total = b1 + b2 + b3 + b4
diskon = total * 7.5/100
hasil_diskon = total - diskon

print('Total Belanja:', total)

if total > 200000:
    print(f'''
Diskon: {diskon}
Total Bayar: {hasil_diskon}
    ''')
else:
    print(f'''
Anda Tidak Dapat Diskon
Total Bayar: {total}
    ''')