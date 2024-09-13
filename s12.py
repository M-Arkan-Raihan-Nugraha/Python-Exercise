s = input('Siswa: ')
n = float(input('Nilai (Rentang Nilai 0-100): '))
if n > 90:
    print('Grade: A')
elif n > 80:
    print('Grade: B')
elif n > 70:
    print('Grade: C')
elif n > 60:
    print('Grade: D')
else:
    print('Grade: E')
