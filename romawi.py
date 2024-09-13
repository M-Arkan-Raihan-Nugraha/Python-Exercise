b = int(input('Masukan Bilangan (1-10): '))

if b == 1:
    print('Angka Romawi: I')
elif b == 2:
    print('Angka Romawi: II')
elif b == 3:
    print('Angka Romawi: III')
elif b == 4:
    print('Angka Romawi: IV')
elif b == 5:
    print('Angka Romawi: V')
elif b == 6:
    print('Angka Romawi: VI')
elif b == 7:
    print('Angka Romawi: VII')
elif b == 8:
    print('Angka Romawi: VIII')
elif b == 9:
    print('Angka Romawi: IX')
elif b == 10:
    print('Angka Romawi: X')
else:
    print('Salah')


def romawi(num):
    # Tabel nilai
    val = [
        50, 40, 30, 20, 10,
        9, 5, 4, 1
    ]
    syb = [
        "L", "XL", "XXX", "XX", "X",
        "IX", "V", "IV", "I"
    ]
    
    romawi = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            romawi += syb[i]
            num -= val[i]
        i += 1
    
    return romawi

# Input pengguna
b = int(input('Masukkan bilangan (1-50): '))
if 1 <= b <= 50:
    print('Angka Romawi:', romawi(b))
else:
    print('Bilangan di luar rentang (1-50)')
