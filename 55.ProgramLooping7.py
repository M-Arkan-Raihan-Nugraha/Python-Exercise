# DIBUAT OLEH: M ARKAN RAIHAN NUGRAHA
# TANGGAL DIBUAT: 06 NOVEMBER 2024
# PROGRAM PENGULANGAN PERTAMBAHAN 1 SAMPAI 5 = 15 SECARA VERTIKAL

print('='*20)
print('PROGRAM LOOPING 7')
print('='*20)

total = 0
for i in range(1, 6, 2):
    print(i, end=' + ' if i < 5 else ' = ')
    total += i

print(total)