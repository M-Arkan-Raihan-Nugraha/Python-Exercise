# DIBUAT OLEH: M ARKAN RAIHAN NUGRAHA
# TANGGAL DIBUAT: 11 OKTOBER 2024
# PROGRAM MENGKONVERSI METER KE INCHI-KAKI-YARD

print('='*25)
print('PROGRAM KONVERSI METER')
print('='*25)

m = int(input('Masukkan Panjang Meter: '))
i = m * 1000 / 25.4
m = m / 25.4
k = m * 100 / 30.48
m = m % 30.48
y = m % 0.9144
m = m % 0.9144

print('Hasil Konversi: ', round(i,2), 'Inchi', round(k,2), 'Kaki', round(y,2), 'Yard')