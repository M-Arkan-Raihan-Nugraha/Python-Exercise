# DIBUAT OLEH: M ARKAN RAIHAN NUGRAHA
# TANGGAL DIBUAT: 05 Oktober 2024
# PROGRAM MENGHITUNG LUAS, KELILING, DAN VOLUME TABUNG

print('='*15)
print('PROGRAM TABUNG')
print('='*15)

def tabung():
    r = float(input("Masukkan Jari-Jari: "))
    t = float(input('Masukan Tinggi: '))
    luas = lambda l: 2 * 3.14 * r**2
    keliling = lambda k: 2 * 3.14 * r
    volume = lambda v: 3.14 * r**2 * t

    print('Keliling\t: ' , keliling(r), 'Cm')
    print('Luas\t\t: ' , luas(r), 'Cm2')
    print('Volume\t\t: ' , volume(r), 'Cm3')

tabung()