# DIBUAT OLEH: M ARKAN RAIHAN NUGRAHA
# TANGGAL DIBUAT: 04 NOVEMBER 2024
# PROGRAM MEMOTONG (CLIPPING) JIKA NILAI HASIL OPERASI PENGOLAHAN CITRA LEBIH DARI 255

print('='*20)
print('PROGRAM CLIPPING')
print('='*20)

nilai = int(input('Masukkan Nilai Hasil Operasi Pengolahan Citra: '))
if nilai > 255:
    nilai = 255
elif nilai < 0:
    nilai = 0
else:
    Salah

print('Hasil Clipping: ', nilai)