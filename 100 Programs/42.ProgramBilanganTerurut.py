# DIBUAT OLEH: M ARKAN RAIHAN NUGRAHA
# TANGGAL DIBUAT: 26 Oktober 2024
# PROGRAM MENGURUTKAN 3 BILANGAN BULAT DARI YANG KECIL KE YANG BESAR

print('='*25)
print('PROGRAM BILANGAN TERURUT')
print('='*25)

x = int(input('Masukkan Bilangan Ke-1: '))
y = int(input('Masukkan Bilangan Ke-2: '))
z = int(input('Masukkan Bilangan Ke-3: '))

if x > y and x > z and y > z:
    print(f'Urutan: {z}, {y}, {x}')
elif y > x and y > z and x > z:
    print(f'Urutan: {z}, {x}, {y}')

elif z > x and z > y and y > x:
    print(f'Urutan: {x}, {y}, {z}')
elif y > x and y > z and z > x:
    print(f'Urutan: {x}, {z}, {y}')

elif z > x and z > y and x > y:
    print(f'Urutan: {y}, {x}, {z}')
elif x > z and x > y and z > y:
    print(f'Urutan: {y}, {z}, {x}')

else:
    print('Bilangan Salah')