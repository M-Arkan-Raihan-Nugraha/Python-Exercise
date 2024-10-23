# DIBUAT OLEH: M ARKAN RAIHAN NUGRAHA
# TANGGAL DIBUAT: 14 SEPTEMBER 2024
# PROGRAM PERINTAH SESUAI WARNA LAMPU LALU LINTAS

print('='*20)
print('PROGRAM LALU LINTAS')
print('='*20)

lampu = input('Masukan Warna Lampu Lalu Lintas: ').lower()

if lampu == 'merah':
    print('Perintah: Berhenti')
elif lampu == 'kuning':
    print('Perintah: Bersiap-siap')
elif lampu == 'hijau':
    print('Perintah: Jalan')
else:
    print('Bukan Warna Lampu Lalu Lintas')