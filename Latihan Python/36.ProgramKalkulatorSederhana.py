# DIBUAT OLEH: M ARKAN RAIHAN NUGRAHA
# TANGGAL DIBUAT: 24 Oktober 2024
# PROGRAM KALKULATOR SEDERHANA

print('='*25)
print('Kalkulator Sederhana')
print('='*25)

o1 = float(input('Masukkan Operand 1: '))
o = input('Masukkan Operator: ')
o2 = float(input('Masukkan Operand 2: '))

if o == '+':
    print('Hasilnya: ', o1 + o2)
elif o == '-':
    print('Hasilnya: ', o1 - o2)
elif o == '*':
    print('Hasilnya: ', o1 * o2)
elif o == '/':
    print('Hasilnya: ', o1 / o2)
elif o == '%':
    print('Hasilnya: ', o1 % o2)
else:
    print('Operator Salah')