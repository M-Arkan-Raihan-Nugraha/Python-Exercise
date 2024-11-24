# DIBUAT OLEH: M ARKAN RAIHAN NUGRAHA
# TANGGAL DIBUAT: 14 SEPTEMBER 2024
# PROGRAM MENGHITUNG LUAS DAN KELILING SEGITIGA

print('='*20)
print('PROGRAM SEGITIGA')
print('='*20)

def segitiga():
    alas = float(input('Masukan Alas: '))
    tinggi = float(input('Masukan Tinggi: '))
    sisimiring = float(input('Masukan Sisi Miring: '))
    luas = lambda l: 1/2 * alas * tinggi
    a = alas
    b = tinggi
    c = sisimiring
    keliling = lambda k: a + b + c

    print('Luas\t\t: ' , luas(alas) , 'Cm2')
    print('Keliling\t: ' , keliling(alas) , 'Cm')

segitiga()