# DIBUAT OLEH: M ARKAN RAIHAN NUGRAHA
# TANGGAL DIBUAT: 23 Oktober 2024
# PROGRAM MENGHITUNG UPAH KARYAWAN

# JKN: JAM KERJA NORMAL
# UL: UANG LEMBUR
# G: GOLONGAN
# JJK: JUMLAH JAM KERJA
# UPJ: UPAH PER JAM
# UT: UPAH TOTAL
# JL: JAM LEMBUR
# UTL: UPAH TOTAL+LEMBUR

print('='*15)
print('PROGRAM UPAH')
print('='*15)

JKN = 48
UL = 3000
g = input('Masukkan Golongan: ')
jjk = float(input('Masukkan Jumlah Jam Kerja: '))

if g in 'aA':
    upj = 4000
elif g in 'bB':
    upj = 5000
elif g in 'cC':
    upj = 6000
elif g in 'dD':
    upj = 7500

if jjk <= JKN:
    ut = jjk * upj
    print('Upah Total: ', ut)
else:
    jl = jjk - JKN
    utl = JKN * upj + jl*UL
    print('Upah Total + Upah Lembur: ', utl)