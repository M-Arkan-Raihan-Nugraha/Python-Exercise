b = int(input('Masukan Nomor Bulan: '))
t = int(input('Masukan Tahun: '))
Januari = 1
Februari = 2
Maret = 3
April = 4
Mei = 5
Juni = 6
Juli = 7
Agustus = 8
September = 9
Oktober = 10
November = 11
Desember = 12

if b == Januari:
    print(f'Bulan Januari Tahun {t} Jumlah Harinya Adalah 31')
elif b == Februari:
    print(f'Bulan Februari Tahun {t} Jumlah Harinya Adalah 29')
elif b == Maret:
    print(f'Bulan Maret Tahun {t} Jumlah Harinya Adalah 30')
elif b == April:
    print(f'Bulan April Tahun {t} Jumlah Harinya Adalah 30')
elif b == Mei:
    print(f'Bulan Mei Tahun {t} Jumlah Harinya Adalah 31')
elif b == Juni:
    print(f'Bulan Juni Tahun {t} Jumlah Harinya Adalah 30')
elif b == Juli:
    print(f'Bulan Juli Tahun {t} Jumlah Harinya Adalah 31')
elif b == Agustus:
    print(f'Bulan Agustus Tahun {t} Jumlah Harinya Adalah 31')
elif b == September:
    print(f'Bulan September Tahun {t} Jumlah Harinya Adalah 30')
elif b == Oktober:
    print(f'Bulan Oktober Tahun {t} Jumlah Harinya Adalah 31')
elif b == November:
    print(f'Bulan November Tahun {t} Jumlah Harinya Adalah 30')
elif b == Desember:
    print(f'Bulan Desember Tahun {t} Jumlah Harinya Adalah 31')
else:
    print('Bukan Nomor Bulan')