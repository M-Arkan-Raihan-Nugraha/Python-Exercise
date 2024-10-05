lampu = input('Masukan Warna Lampu Lalu Lintas: ').lower()

if lampu == 'merah':
    print('Berhenti')
elif lampu == 'kuning':
    print('Bersiap-siap')
elif lampu == 'hijau':
    print('Jalan')
else:
    print('Bukan Warna Lampu Lalu Lintas')