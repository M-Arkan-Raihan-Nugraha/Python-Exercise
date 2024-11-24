# DIBUAT OLEH: M ARKAN RAIHAN NUGRAHA
# TANGGAL DIBUAT: 24 Oktober 2024
# PROGRAM MENENTUKAN JUMLAH HARI DALAM SATU BULAN

print('='*20)
print('PROGRAM JUMLAH HARI')
print('='*20)

b = int(input('Masukkan Nomor Bulan: '))
t = int(input('Masukkan Tahun: '))

if b in [1,3,5,7,8,10,12]:
    jh = 31
elif b in [4,6,9,11]:
    jh = 30
elif b == 2:
    if (t % 4 == 0 and t % 100 != 0) or (t % 400 == 0):
        jh = 29
    else:
        jh = 28
        
print('Jumlah Hari: ', jh)