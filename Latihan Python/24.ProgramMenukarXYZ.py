# DIBUAT OLEH: M ARKAN RAIHAN NUGRAHA
# TANGGAL DIBUAT: 10 Oktober 2024
# PROGRAM MENUKAR NILAI XYZ MENJADI YZX

print('='*25)
print('PROGRAM MENUKAR XYZ')
print('='*25)

x = int(input('Masukan X: '))
y = int(input('Masukan Y: '))
z = int(input('Masukan Z: '))

a = x
x = y
y = z
z = a

print('XYZ: ', a, x, y)
print('YZX: ', x, y, z)