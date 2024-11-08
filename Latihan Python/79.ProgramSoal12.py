# DIBUAT OLEH: M ARKAN RAIHAN NUGRAHA
# TANGGAL DIBUAT: 08 NOVEMBER 2024
# PROGRAM MENENTUKAN GRADE DARI SISWA BERDASARKAN INPUTAN

print('='*20)
print('PROGRAM SOAL 12')
print('='*20)

s = input('Masukkan Nama Siswa: ')
n = float(input('Masukkan Nilai (Rentang Nilai 0-100): '))
if n > 90:
    print('Grade: A')
elif n > 80:
    print('Grade: B')
elif n > 70:
    print('Grade: C')
elif n > 60:
    print('Grade: D')
else:
    print('Grade: E')