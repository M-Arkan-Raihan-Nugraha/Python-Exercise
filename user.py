print('''
\033[30m
======
Login
======
''')

u = input('Masukkan Username: ')
p = input('Masukkan Password: ')

# User
if u == 'admin':
    print('Username Benar')
else:
    print('Username Salah')

# Pass
if (p == 'nimda123'):
    print('Password Benar')
else:
    print('Password Salah')