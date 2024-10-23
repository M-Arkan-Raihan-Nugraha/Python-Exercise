# DIBUAT OLEH: M ARKAN RAIHAN NUGRAHA
# TANGGAL DIBUAT: 05 Oktober 2024
# PROGRAM MENGHITUNG LUAS PERMUKAAN, KELILING, DAN VOLUME BOLA

print('='*15)
print('PROGRAM BOLA')
print('='*15)

def bola():
    r = float(input("Masukkan Jari-Jari: "))
    luas = lambda l: 4 * 3.14 * r**2
    keliling = lambda k: 2 * 3.14 * r
    volume = lambda v: 4/3 * 3.14 * r**3

    print('Keliling\t: ' , round(keliling(r),2), 'Cm')
    print('Luas Permukaan\t: ' , round(luas(r),2), 'Cm2')
    print('Volume\t\t: ' , round(volume(r),2), 'Cm3')

bola()