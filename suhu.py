print('''
===========================
PROGRAM KONVERSI SUHU
===========================
''')

c = input('Masukkan suhu (dalam celcius) :')
f = 9/5  * int(c) + 32
r = 4/5 * int(c)

print(f'''
Suhu dalam Fahrenheit : {f} F
Suhu dalam Reamur : {r} R
''')