# DIBUAT OLEH: M ARKAN RAIHAN NUGRAHA
# TANGGAL DIBUAT: 05 Oktober 2024
# PROGRAM MENGHITUNG LUAS PERMUKAAN, KELILING, DAN VOLUME KERUCUT

print('='*15)
print('PROGRAM KERUCUT')
print('='*15)

def kerucut():
    r = float(input("Masukkan Jari-Jari: "))
    t = float(input('Masukan Tinggi: '))
    s = float(input('Masukan Garis Pelukis: '))
    luas = lambda l: 3.14 * r * (r + s)
    keliling = lambda k: 2 * 3.14 * r
    volume = lambda v: 1/3 * 3.14 * r**2 * t

    print('Keliling\t: ' , keliling(r), 'Cm')
    print('Luas Permukaan\t: ' , luas(r) , 'Cm2')
    print('Volume\t\t: ' , volume(r) , 'Cm3')

kerucut()