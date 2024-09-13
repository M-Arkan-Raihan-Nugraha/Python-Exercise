TAHUN_HARI = 30 * 12 
hari = int(input('Hari : '))
tahun = int(hari / 365)
hari = hari % TAHUN_HARI
bulan = int(hari / 30)
hari = hari % 30

print(tahun, 'tahun' , bulan , 'bulan' , hari , 'hari')