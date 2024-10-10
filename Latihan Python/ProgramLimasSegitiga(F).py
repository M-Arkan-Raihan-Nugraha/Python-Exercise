# DIBUAT OLEH: M ARKAN RAIHAN NUGRAHA
# TANGGAL DIBUAT: 05 Oktober 2024
# PROGRAM MENGHITUNG LUAS PERMUKAAN DAN VOLUME LIMAS SEGITIGA

print('='*25)
print('PROGRAM LIMAS SEGITIGA')
print('='*25)

def limassegitiga():
    la = float(input("Masukkan Luas Alas: "))
    ls = float(input('Masukan Luas Selubung: '))
    t = float(input('Masukan Tinggi: '))
    luas = lambda l: la + ls
    volume = lambda v: 1/3 * la * t

    print('Luas Permukaan\t: ' , round(luas(la),2), 'Cm2')
    print('Volume\t\t: ' , round(volume(la),2), 'Cm3')

limassegitiga()