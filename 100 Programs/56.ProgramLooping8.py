# DIBUAT OLEH: M ARKAN RAIHAN NUGRAHA
# TANGGAL DIBUAT: 06 NOVEMBER 2024
# PROGRAM PENGULANGAN PERTAMBAHAN 1 SAMPAI 5 = 15 SECARA VERTIKAL

print('='*20)
print('PROGRAM LOOPING 8')
print('='*20)

i = 2
total = 0
while i <= 10:
    print(i, end=' + ' if i < 10 else ' = ')
    total += i
    i += 2

print(total)