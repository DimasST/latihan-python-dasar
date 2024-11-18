# latihan percabangan kalkulator sederhana

print(10*'=')
print('Kalkulator Sederhana')
print(10*'=')

angka_1 = float(input('Masukan angka 1 :'))
operator = input('Masukan operator (+,-,x,/) :')
angka_2 = float(input('Masukan angka 2 :'))

if operator == '+':
    hasil = angka_1 + angka_2
    print(f'Hasilnya : {hasil}')
elif angka_1 != float or angka_2 != float:
    print("masukin nya angka woi")
elif operator == '-':
    hasil = angka_1 - angka_2
    print(f'Hasilnya : {hasil}')
elif operator == 'x' or operator == '*':
    hasil = angka_1 * angka_2
    print(f'Hasilnya : {hasil}')
elif operator == '/':
    hasil = angka_1 / angka_2
    print(f'Hasilnya : {hasil}')
else:
    print('Masukin yang bener dong')
print('program selesai')