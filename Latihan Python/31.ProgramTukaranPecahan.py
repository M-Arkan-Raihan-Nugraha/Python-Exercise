# DIBUAT OLEH: M ARKAN RAIHAN NUGRAHA
# TANGGAL DIBUAT: 11 OKTOBER 2024
# PROGRAM MENGHITUNG TUKARAN PECAHAN UANG KELIPATAN 25

print('='*25)
print('PROGRAM TUKARAN PECAHAN')
print('='*25)

u = int(input('Masukan Nilai Uang (Rupiah) Kelipatan 25: '))

# 1000, 500, 100, 50, 25
tp1 = u / 1000
u = u % 1000
tp2 = u / 500
u = u % 500
tp3 = u / 100
u = u % 100
tp4 = u / 50
u = u % 50
tp5 = u / 25
u = u % 25

print(f'''Setara Dengan: 
{int(tp1)} buah pecahan Rp1000
Ditambah {int(tp2)} buah pecahan Rp500
Ditambah {int(tp3)} buah pecahan Rp100
Ditambah {int(tp4)} buah pecahan Rp50
Ditambah {int(tp5)} buah pecahan Rp25
''')