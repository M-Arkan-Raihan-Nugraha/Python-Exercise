cm = int(input('Jarak Cm: '))
km = cm / 100000
cm = cm % 100000
m = cm / 100
cm = cm % 100

print('Berarti = ' , int(km) , 'km + ' , int(m) , 'm + ' , int(cm) , 'cm')