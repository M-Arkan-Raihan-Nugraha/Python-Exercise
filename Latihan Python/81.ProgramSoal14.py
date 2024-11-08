# DIBUAT OLEH: M ARKAN RAIHAN NUGRAHA
# TANGGAL DIBUAT: 08 NOVEMBER 2024
# PROGRAM MENENTUKAN HURUF TERMASUK HURUF VOKAL ATAU KONSONAN

print('='*20)
print('PROGRAM SOAL 14')
print('='*20)

h = input('Masukan Suatu Huruf A-Z: ')
if h in 'aiueoAIUEO':
    print('Huruf Tersebut Termasuk Huruf Vokal')
elif h.isdigit():
    print('Bukan Berupa Huruf')
else:
    print('Huruf Tersebut Termasuk Huruf Konsonan')