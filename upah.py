JKN = 48
UL = 3000
g = input('Masukan Golongan: ')
jjk = float(input('Masukan Jumlah Jam Kerja: '))

if g in 'aA':
    upj = 4000
elif g in 'bB':
    upj = 5000
elif g in'cC':
    upj = 6000
elif g in'dD':
    upj = 7500

if jjk <= JKN:
    ut = jjk * upj
    print('Upah Total: ' , ut)
else:
    jl = jjk - JKN
    utl = JKN * upj + jl*UL
    print('Upah Total + Upah Lembur: ' , utl)