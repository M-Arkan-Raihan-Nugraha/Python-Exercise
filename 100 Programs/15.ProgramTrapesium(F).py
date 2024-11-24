# DIBUAT OLEH: M ARKAN RAIHAN NUGRAHA
# TANGGAL DIBUAT: 24 SEPTEMBER 2024
# PROGRAM MENGHITUNG LUAS DAN KELILING TRAPESIUM

print('='*25)
print('PROGRAM TRAPESIUM')
print('='*25)

def trapesium():
    a = float(input("Masukkan Sisi Sejajar Pertama (a): "))
    b = float(input("Masukkan Sisi Sejajar Kedua (b): "))
    c = float(input("Masukkan Sisi Miring Pertama (c): "))
    d = float(input("Masukkan Sisi Miring kedua (d): "))
    tinggi = float(input("Masukkan Tinggi: "))
    luas = lambda l: 1/2 * (a + b) * tinggi
    keliling = lambda k: a + b + c + d

    print('Luas\t\t: ' , luas(a), 'Cm2')
    print('Keliling\t: ' , keliling(a), 'Cm')

trapesium()