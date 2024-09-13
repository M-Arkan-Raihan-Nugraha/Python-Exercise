p = int(input('Masukan Nilai Hasil Pengolahan Citra: '))
if p > 255:
    p = 255
elif p < 0:
    p = 0

print('Hasil Clipping: ' , p)