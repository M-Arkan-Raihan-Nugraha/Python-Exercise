# DIBUAT OLEH: M ARKAN RAIHAN NUGRAHA
# TANGGAL DIBUAT: 07 NOVEMBER 2024
# PROGRAM PENGULANGAN HURUF A SAMPAI E SEBANYAK 5 KALI SECARA VERTIKAL

print('='*20)
print('PROGRAM LOOPING 17')
print('='*20)

huruf = 'a'
i = 0

while i < 5:
    print(huruf * 5)
    huruf = chr(ord(huruf) + 1)
    i += 1