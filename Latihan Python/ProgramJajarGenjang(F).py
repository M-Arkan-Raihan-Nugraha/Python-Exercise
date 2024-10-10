# DIBUAT OLEH: M ARKAN RAIHAN NUGRAHA
# TANGGAL DIBUAT: 24 SEPTEMBER 2024
# PROGRAM MENGHITUNG LUAS DAN KELILING JAJAR GENJANG

print('='*25)
print('PROGRAM JAJAR GENJANG')
print('='*25)

def jajargenjang():
    alas = float(input('Masukan Alas: '))
    tinggi = float(input('Masukan Tinggi: '))
    sisimiring = float(input('Masukan Sisi Miring: '))
    luas = lambda l: alas * tinggi
    keliling = lambda k: 2 * (alas + tinggi)

    print('Luas\t\t: ' , luas(alas), 'Cm2')
    print('Keliling\t: ' , keliling(alas), 'Cm')

jajargenjang()