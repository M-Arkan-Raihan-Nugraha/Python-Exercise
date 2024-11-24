# DIBUAT OLEH: M ARKAN RAIHAN NUGRAHA
# TANGGAL DIBUAT: 26 Oktober 2024
# PROGRAM MENKONVERSI KARAKTER DIGIT ('0'..'9') MENJADI INTEGER (0..9)

print('='*25)
print('PROGRAM KONVERSI DIGIT')
print('='*25)

a = input('Masukkan Karakter Digit (0-9): ')
if a in '0123456789':
    print('Hasil Konversi: ', int(a))
else:
    print('Hasil Konversi: ', int(-99))