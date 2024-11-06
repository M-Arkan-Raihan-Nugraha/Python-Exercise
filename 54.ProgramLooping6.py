# DIBUAT OLEH: M ARKAN RAIHAN NUGRAHA
# TANGGAL DIBUAT: 06 NOVEMBER 2024
# PROGRAM PENGULANGAN PERTAMBAHAN 1 SAMPAI 5 = 15 SECARA VERTIKAL

print('='*20)
print('PROGRAM LOOPING 6')
print('='*20)

i = 1
total = 0
while i <= 5:
    print(i)
    total += i
    i += 1
    if i > 5:
        print('--- +')
        
print(total)