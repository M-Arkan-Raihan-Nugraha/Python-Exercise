# DIBUAT OLEH: M ARKAN RAIHAN NUGRAHA
# TANGGAL DIBUAT: 22 NOVEMBER 2024
# PROGRAM MEMBAGI TIM FUTSAL PARA PEMAIN SECARA ACAK

print('='*20)
print('FUTSAL TEAM DIVIDER')
print('='*20)

import random

pemain = input('Masukkan Nama-nama Pemain (Pisahkan dengan spasi): ').split(' ')
pemain = [nama.strip() for nama in pemain]
random.shuffle(pemain)

def bagi_tim(pemain, ukuran_tim=5):
    tim_list = []
    for i in range(0, len(pemain), ukuran_tim):
        tim_list.append(pemain[i:i + ukuran_tim])
    return tim_list

tim_list = bagi_tim(pemain)

print('Hasil Pembagian Tim')
for idx, tim in enumerate(tim_list):
    print(f'Tim {chr(65 + idx)}: {', '.join(tim)}')