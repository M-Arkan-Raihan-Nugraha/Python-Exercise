# DIBUAT OLEH: M ARKAN RAIHAN NUGRAHA
# TANGGAL DIBUAT: 26 Oktober 2024
# PROGRAM MENENTUKAN JENIS SEGITIGA MENGGUNAKAN RUMUS PHYTAGORAS

print('='*25)
print('PROGRAM JENIS SEGITIGA')
print('='*25)

a = float(input('Masukkan Sisi A: '))
b = float(input('Masukkan Sisi B: '))
c = float(input('Masukkan Sisi C: '))
print('Jenis Segitiga:')

if c*c == a*a + b*b:
    print('Segitiga Siku-siku')
elif c*c < a*a + b*b:
    print('Segitiga Lancip')
elif c*c > a*a + b*b:
    print('Segitiga Tumpul')
else:
    print('Salah')