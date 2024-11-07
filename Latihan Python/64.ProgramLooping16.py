# DIBUAT OLEH: M ARKAN RAIHAN NUGRAHA
# TANGGAL DIBUAT: 07 NOVEMBER 2024
# PROGRAM PENGULANGAN BINTANG YANG BERTAMBAH DARI 1 SAMPAI 5 DAN BERKURANG DARI 4 SAMPAI 1 MENYUSUN BERBENTUK SEGITIGA

print('='*20)
print('PROGRAM LOOPING 16')
print('='*20)

i = 0
while i < 5:
    print(' ' * (5 - i - 1) + '* ' * (i + 1))
    i += 1

i = 4
while i > 0:
    print(' ' * (5 - i) + '* ' * i)
    i -= 1