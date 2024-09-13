print('''
\033[95m
===========================
JARAK LENSA OBJEKTIF DAN LENSA OKULER
===========================
''')

fob = float(input('Masukan Fokus Lensa Objektif:'))
fp = float(input('Masukan Fokus Lensa Pembalik:'))
fok = float(input('Masukan Fokus Lensa Okuler:'))
d = fob + (4 * fp) + fok

print('\033[95m\033[01mJarak Lensa Objektif Dan Lensa Okuler:', round(d))