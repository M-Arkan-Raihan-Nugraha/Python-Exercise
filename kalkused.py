o1 = float(input('Operand 1: '))
o = input('Operator: ')
o2 = float(input('Operand 2: '))
h = o1 , o , o2

if o == '+':
    print('Hasilnya: ' , o1 + o2)
elif o == '-':
    print('Hasilnya: ' , o1 - o2)
elif o == '*':
    print('Hasilnya: ' , o1 * o2)
elif o == '/':
    print('Hasilnya: ' , o1 / o2)
else:
    print('Bukan Operator')