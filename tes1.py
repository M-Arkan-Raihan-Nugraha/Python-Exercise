print('='*40)
print('RUMUS KERUCUT')
print('='*40)

phi = 3.14
r = float(input('Masukan Jari Jari: '))
s = float(input('Masukan Sisi: '))
t = float(input('Masukan Tinggi: '))

ls = 3.14 * r * s
lp = 3.14 * r * s + 3.14 * r * r
v = 1/3 * 3.14 * r * r * t

print('Luas Selimut: ' , round(ls,2))
print('Luas Permukaan: ' , round(lp))
print('Volume: ' , round(v))