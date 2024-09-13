nb = int(input('Masukan Nilai Belanja: '))
sisa = nb % 25

if sisa != 0:
    print('Total Belanja: ' , nb - sisa)
else:
    print('Total Belanja: ' , nb)
