# DIBUAT OLEH: M ARKAN RAIHAN NUGRAHA
# TANGGAL DIBUAT: 08 NOVEMBER 2024
# PROGRAM MENENTUKAN NILAI TERKECIL DAN TERBESAR MENGGUNAKAN PENGKONDISIAN

print('='*20)
print('PROGRAM SOAL 13')
print('='*20)

x = int(input('Masukan x: '))
y = int(input('Masukan y: '))
z = int(input('Masukan z: '))

if x > y and x > z:
    print('Nilai Terbesar: ' , x)

if x < y and x < z:
    print('Nilai Terkecil: ' , x)

if y > x and y > z:
    print('Nilai Terbesar: ' , y)

if y < x and y < z:
    print('Nilai Terkecil: ' , y)

if z > x and z > y:
    print('Nilai Terbesar: ' , z)
    
else:
    print('Nilai Terkecil: ' , z)