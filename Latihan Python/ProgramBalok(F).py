# DIBUAT OLEH: M ARKAN RAIHAN NUGRAHA
# TANGGAL DIBUAT: 05 Oktober 2024
# PROGRAM MENGHITUNG LUAS PERMUKAAN, KELILING, DAN VOLUME BALOK

print('='*15)
print('PROGRAM BALOK')
print('='*15)

def balok():
    p = float(input("Masukkan Panjang: "))
    l = float(input('Masukan Lebar: '))
    t = float(input('Masukan Tinggi: '))
    luas = lambda l: 2 * (p*l + p*t + l*t)
    keliling = lambda k: p * l * t
    volume = lambda v: 4 * (p+l+t)

    print('Keliling\t: ' , keliling(p), 'Cm')
    print('Luas Permukaan\t: ' , luas(p), 'Cm2')
    print('Volume\t\t: ' , volume(p), 'Cm3')

balok()