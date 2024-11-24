# list bersarang / 2d list dalam list

angka_1 = [1,2,3]
angka_2 = [4,5,6]

angka = [angka_1,angka_2]
print(f'list biasa : {angka_1,angka_2}')
print(f'list 2D : {angka}')

peserta_0 = ['dimas',17,'Pria']
peserta_1 = ['dawam',12,'Pria']
peserta_2 = ['icip',23,'Pria']

list_peserta = [peserta_0,peserta_1,peserta_2]

print(f'list peserta : {list_peserta}')

for peserta in list_peserta:
    print(f'nama \t: {peserta[0]}')
    print(f'umur \t: {peserta[1]}')
    print(f'jenis kelamin \t: {peserta[2]}\n')

# dengan refrence
list_copy = list_peserta.copy()
print(f'list peserta : {list_copy}')
peserta_0[0] = 'ucup'
print(f'list peserta : {list_copy}')
print(f'list peserta : {list_peserta}')