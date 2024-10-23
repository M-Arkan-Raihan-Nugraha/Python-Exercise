# DIBUAT OLEH: M ARKAN RAIHAN NUGRAHA
# TANGGAL DIBUAT: 23 Oktober 2024
# PROGRAM MENENTUKAN INDEKS NILAI

print('='*25)
print('PROGRAM INDEKS NILAI')
print('='*25)

n = float(input('Masukkan Nilai Ujian: '))
if n >= 80:
    print('Indeks Nilai: A')
elif n >= 70 and n < 80:
    print('Indeks Nilai: B')
elif n >= 55 and n < 70:
    print('Indeks Nilai: C')
elif n >= 40 and n < 55:
    print('Indeks Nilai: D')
else:
    print('Indeks Nilai: E')