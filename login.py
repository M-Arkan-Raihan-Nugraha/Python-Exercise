USERNAME = 'tempatlahirbetta@gmail.com'
PASSWORD = '12345678'

username = input('Masukan Username: ')
password = input('Masukan Password: ')

if username != USERNAME:
    print('Username Tidak Tersedia')
elif username == USERNAME and password != PASSWORD:
    print('Password Salah')
else:
    print('Selamat Datang' , username)