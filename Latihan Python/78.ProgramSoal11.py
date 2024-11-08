# DIBUAT OLEH: M ARKAN RAIHAN NUGRAHA
# TANGGAL DIBUAT: 08 NOVEMBER 2024
# PROGRAM MENAMPILKAN HASIL DARI DISKON DAN TOTAL BARANG YANG HARUS DIBAYAR

print('='*20)
print('PROGRAM SOAL 11')
print('='*20)

t = float(input('Masukkan Total Harga Barang: '))
d = t * 5/100
tb = t - d

if t > 100000:
    print(f''' 
Hasil Dari Diskon: {d}
Total Barang Yang Harus Dibayar: {tb}
    ''')
else:
    print('Total Barang Yang Harus Dibayar: ' , t)