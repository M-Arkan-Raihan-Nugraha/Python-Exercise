# DIBUAT OLEH: M ARKAN RAIHAN NUGRAHA
# TANGGAL DIBUAT: 11 OKTOBER 2024
# PROGRAM MENENTUKAN BERAT BADAN IDEAL

print('='*20)
print('PROGRAM BB IDEAL')
print('='*20)

tb = float(input('Masukkan Tinggi Badan (Cm): '))
bbi = tb - 100
bbi1 = 10 / 100 * bbi
bbi2 = bbi - bbi1

print('BB Yang Ideal Untuk TB Tersebut: ', bbi2, 'Kg')