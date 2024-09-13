print('Tanggal Pertama (dd:mm:yy)')
hari = int(input('Hari: '))
bulan = int(input('Bulan: '))
tahun = int(input('Tahun: '))
hari1 = hari + bulan * 30 + tahun * 365

print('Tanggal Kedua (dd:mm:yy)')
hari = int(input('Hari: '))
bulan = int(input('Bulan: '))
tahun = int(input('Tahun: '))
hari2 = hari + bulan * 30 + tahun * 365

hari = hari2 - hari1
tahun = hari / 365
bulan = hari % 365 / 30
hari = hari % 365 / 30

print('Jarak Kedua Tanggal Tersebut: ' , tahun, 'tahun' , bulan , 'bulan' , hari , 'hari')