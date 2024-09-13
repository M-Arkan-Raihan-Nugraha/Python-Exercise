t = float(input('Total Harga Barang: '))
d = t * 5/100
tb = t - d

if t > 100000:
    print(f''' 
Hasil Dari Diskon: {d}
Total Barang Yang Harus Dibayar: {tb}
    ''')
else:
    print('Total Barang Yang Harus Dibayar: ' , t)