# DIBUAT OLEH: M ARKAN RAIHAN NUGRAHA
# TANGGAL DIBUAT: 24 SEPTEMBER 2024
# PROGRAM MENGHITUNG LUAS DAN KELILING LINGKARAN

print('='*20)
print('PROGRAM LINGKARAN')
print('='*20)

def lingkaran():
    r = float(input('Masukan Jari-Jari: '))
    luas = lambda l: 3.14 * r * r
    keliling = lambda k: 2 * 3.14 * r

    print('Luas\t\t: ' , luas(r), 'Cm2')
    print('Keliling\t: ' , keliling(r), 'Cm')

lingkaran()