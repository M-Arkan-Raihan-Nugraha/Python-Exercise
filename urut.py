x = int(input('Masukan Bilangan Ke 1: '))
y = int(input('Masukan Bilangan Ke 2: '))
z = int(input('Masukan Bilangan Ke 3: '))

if x > y and x > z and y > z:
  print('Urutan:' , z , y , x)
elif y > x and y > z and x > z:
  print('Urutan:' , z , x , y)
elif z > x and z > y and y > x:
  print('Urutan:' , x , y , z)
elif y > x and y > z and z > x:
  print('Urutan:' , x , z , y)
elif z > x and z > y and x > y:
  print('Urutan:' , y , x , z)
elif x > z and x > y and z > y:
  print('Urutan:' , y , z , x)
else:
    print('Bilangan Salah')