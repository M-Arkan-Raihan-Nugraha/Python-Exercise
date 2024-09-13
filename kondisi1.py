sa = input('Masukan Kondisi Air: ').lower()
if sa == 'mendidih':
    print('Matikan Api Kompor')
else:
    print('Salah')

sr = int(input('Masukan Suhu Ruangan: '))
if sr > 50:
    print('Bunyikan Alarm Tanda Bahaya')
else:
    print('Salah!')

m = input('Masukan Kondisi Mobil: ').lower()
if m == 'rusak':
    print('Naik Angkot')
else:
    print('Salah!')

x = int(input('Masukan Bilangan x: '))
if x % 2 == 0:
    print(x , 'Bilangan Genap')
else:
    print('Salah!')