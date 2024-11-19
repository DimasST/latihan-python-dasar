# continue, pass, break

# pass
angka = 0 
while angka < 5:
    angka += 1
    print(f'angka sekarang ; {angka}')
    pass # melewatkan semua aksi di dalam while
print('finish\n')

# continue 
angka1 = 0
while angka1 < 5:
    angka1 += 1
    print(f'angka1 sekarang ; {angka1}')
    if angka1 == 3:
        print('wett')
        continue # mengulang lagi ke awal dan mengabaikan statement selanjutnya
    print('whoop')
print('finish')

# break 

#contoh 1
angka2 = 0
while angka2 < 5:
    angka2 += 1
    print(f'angka2 sekarang ; {angka2}')
    if angka2 == 3:
        print('wett')
        break
print('finish')

#contoh2 
data_int = int(input('masukan angka : '))

angka = 0
while angka < 5:
    angka += 1
    print(f'angka sekarang : {angka}')
    if angka == data_int:
        print('wett')
        break
    print('whoop')
print('finish')