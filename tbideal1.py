tb = float(input('Masukan Tinggi Badan: '))
bb = float(input('Masukan Berat Badan: '))
bbi = (tb - 100) - ((tb - 100)*0.1)
bbimax = bbi + 2
bbimin = bbi - 2

print('Berat Badan Ideal: ' , bbimin , '<-->' , bbimax)
if bb <= bbimax and bb >= bbimin:
    print('Ideal')
else:
    print('Tidak Ideal')