# Inputkan total belanja, apabila total belanja 100k ke atas maka tuliskan 'Anda mendapatkan diskon' dan sebaliknya
print('''
\033[36m
=============
Total Belanja
=============
''')

t = int(input('Masukan Total Belanja: '))

if t > 100000:
    print('Anda Mendapatkan Diskon')
else:
    print('Anda Tidak Mendapatkan Diskon')
