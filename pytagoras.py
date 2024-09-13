a = int(input('Masukan Sisi A: '))
b = int(input('Masukan Sisi B: '))
c = int(input('Masukan Sisi C: '))

if c*c == a*a + b*b:
    print('Segitiga Siku-siku')
elif c*c < a*a + b*b:
    print('Segitiga Lancip')
elif c*c > a*a + b*b:
    print('Segitiga Tumpul')
else:
    print('Salah')