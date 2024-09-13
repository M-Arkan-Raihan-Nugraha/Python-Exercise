lampu = input('Masukan Warna Lampu Lalu Lintas: ').lower()

if lampu == 'merah':
    print('Berhenti')
elif lampu == 'kuning':
    print('Bersiap-siap')
elif lampu == 'hijau':
    print('Jalan')
else:
    print('Bukan Warna Lampu Lalu Lintas')


sa = input('Masukan Kondisi Air: ')
sr = int(input('Masukan Suhu Ruangan: '))
m = input('Masukan Kondisi Mobil: ')
x = input('Masukan x')

if sa == 'mendidih':
    print('Matikan Api Kompor')
elif sr > 50:
    print('Bunyikan Alarm Tanda Bahaya')
elif m == 'rusak':
    print('Naik Angkot')
elif x % 2 == 0:
    print(x , 'Bilangan Genap')
else:
    print('Salah!')