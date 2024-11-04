# DIBUAT OLEH: M ARKAN RAIHAN NUGRAHA
# TANGGAL DIBUAT: 04 NOVEMBER 2024
# PROGRAM MENENTUKAN BERAT BADAN IDEAL V2

print('='*20)
print('PROGRAM BB IDEAL V2')
print('='*20)

tb = float(input('Masukkan Tinggi Badan: '))
bb = float(input('Masukkan Berat Badan: '))

bbi = (tb-100) - ((tb-100)*0.1)
bbimax = bbi + 2
bbimin = bbi - 2

if bb <= bbimax and bb >= bbimin:
    print('Ideal')
else:
    print('Tidak Ideal')

print('Berat Badal Ideal: ', bbimin, '<-->', bbimax)