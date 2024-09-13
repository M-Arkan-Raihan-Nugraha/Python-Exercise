h = input('Masukan Suatu Huruf A-Z: ')
if h in 'aiueo':
    print('Huruf Tersebut Termasuk Vokal')
elif h.isdigit():
    print('Bukan Berupa Huruf')
else:
    print('Huruf Tersebut Termasuk Konsonan')