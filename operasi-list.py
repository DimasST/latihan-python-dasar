# operasi list

data_angka = [1,4,2,4,5,6,3,5,6,8,9,0]

print(f'data angka : \n{data_angka}')

# count data
jml_data4 = data_angka.count(3)
print(f'jumlah angka 4 dalam data : \n{jml_data4}')

# ambil posisi data
data = ['dimas','otong','ucup']
print(f'data : \n{data}')

index_dimas = data.index('dimas')
print(f'data dimas ada di index : \n{index_dimas}')

# sort data

print(f'data sebelum di sort \n{data_angka}')
data_angka.sort()
print(f'data setelah di sort : \n{data_angka}')
print(f'data : \n{data}')
data.sort()
print(f'data setelah di sort : \n{data}')

# membalikan data yang udah si sort
data.reverse()
print(f'data setelah di reverse: \n{data}')
data_angka.reverse()
print(f'data setelah di reverse \n{data_angka}')