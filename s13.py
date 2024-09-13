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