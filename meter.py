m = int(input('Panjang Meter: '))
mm = m * 1000
cm = m * 100
inc = mm / 25.4
k = cm / 30.48
y = m / 0.9144

print(f'''
Inchi: {round(inc,2)}
Kaki: {round(k,2)} 
Yard: {round(y,2)}
''')