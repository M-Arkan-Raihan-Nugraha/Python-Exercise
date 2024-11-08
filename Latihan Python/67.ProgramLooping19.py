# DIBUAT OLEH: M ARKAN RAIHAN NUGRAHA
# TANGGAL DIBUAT: 08 NOVEMBER 2024
# PROGRAM PENGULANGAN MENGHITUNG JUMLAH DAN RATA-RATA BERDASARKAN INPUT NILAI

print('='*20)
print('PROGRAM LOOPING 19')
print('='*20)

nilai = input('Masukkan Nilai (Pisahkan Dengan Spasi): ').split()
nilai = [int(x) for x in nilai]
jumlah = 0
i = 0

while i < len(nilai):
    jumlah += nilai[i]
    i += 1

rata2 = jumlah / len(nilai)
print('Jumlah: ', jumlah)
print('Rata-Rata: ', rata2)