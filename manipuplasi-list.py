# operator manipulasi data list

data = ['dimas', 'ucup', 'otong']

# mengambil nilai data pertama 
data_pertama = data[0]
print(f'data pertama : \n{data_pertama}')

# mengambil data terakhir
data_terakhir = data[-1]
print(f'data terakhir : \n{data_terakhir}')

# mengambil info panjang/jumlah data
panjang_data = len(data)
print(f'panjang data : \n{panjang_data}')

## manipulasi data list
print(f'data sebelum di rubah : \n{data}')

# menambah data
data.insert(1,'ijik')
print(f'data setelah ditambah : \n{data}') # (index,datanya)

# manmbah data di akhir list 
data.append('konte')
print(f'data setelah ditambah di akhir : \n{data}')

# menggabungkan 2 list
data_baru = ['jike', 'koliu']
data.extend(data_baru)
print(f'setelah ditambah list baru : \n{data}')

# merubah data 
data[2] = 'haji'
print(f'data rubah : \n{data}')

# meremove data
data.remove('otong')
print(f'data setelah dihapus : \n{data}')

# meremove data paling belakang
data_akhir = data.pop()
print(f'data setelah dihapus : \n{data}')

print(data_akhir)