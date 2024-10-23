# DIBUAT OLEH: M ARKAN RAIHAN NUGRAHA
# TANGGAL DIBUAT: 11 OKTOBER 2024
# PROGRAM MENGKONVERSI CM KE KM-M-CM

print('='*20)
print('PROGRAM KONVERSI CM')
print('='*20)

cm = int(input('Masukkan Panjang Cm: '))
km = cm / 100000
cm = cm % 100000
m = cm / 100
cm = cm % 100

print('Hasil Konversi: ', int(km), 'Km', int(m), 'M', int(cm), 'Cm')