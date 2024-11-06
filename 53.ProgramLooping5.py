# DIBUAT OLEH: M ARKAN RAIHAN NUGRAHA
# TANGGAL DIBUAT: 06 NOVEMBER 2024
# PROGRAM PENGULANGAN PERTAMBAHAN 1 SAMPAI 5 = 15 SECARA HORIZONTAL

print('='*20)
print('PROGRAM LOOPING 5')
print('='*20)

i = 1
total = 0
while i <= 5:
    if i < 5:
        print(i, end=' + ')
    else:
        print(i, end=' = ')
    total += i
    i += 1

print(total)