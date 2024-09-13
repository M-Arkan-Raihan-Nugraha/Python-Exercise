print(f'''
============================================
Dapat Diskon 5% Kalau Belanja Minimal 100K
============================================
''')


total = float(input('Total Belanja: '))
diskon = total * 5/100
hasil_diskon = total - diskon
if total > 100000:
    print(f'''
Diskon: {diskon}
Total Bayar: {hasil_diskon}
    ''')
else:
    print(f'''
Anda Tidak Dapat Diskon
Total Bayar: {total}
    ''')