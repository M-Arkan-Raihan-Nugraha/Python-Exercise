# DIBUAT OLEH: M ARKAN RAIHAN NUGRAHA
# TANGGAL DIBUAT: 08 NOVEMBER 2024
# PROGRAM PENGULANGAN TABEL PERKALIAN BERDASARKAN INPUT NILAI

print('='*20)
print('PROGRAM LOOPING 20')
print('='*20)

n = int(input('Masukkan Jumlah Perkalian: '))
i = 1
while i <= n:
    j = 1
    while j <= n:
        print(f'{i * j:4}', end=' ')
        j += 1
    print()
    i += 1