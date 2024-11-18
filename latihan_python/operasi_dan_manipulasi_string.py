# operasi dan manipulasi string

# 1. Menyambung data string (concatenate)

nama_pertama = "ucup"
nama_tengah = "b"
nama_terakhir = "salim"

nama_lengkap = nama_pertama + " " + nama_tengah + " " + nama_terakhir
print("nama lengkapnya adalah : ", nama_lengkap)

# 2. Menghitung panjang string
panjang = len(nama_lengkap)
print('panjang '+nama_lengkap+'adalah '+str(panjang))

# 3. Operasi untuk string

# Mengecek apakah ada komponen char string dalam string
b = 'b'
status = b in nama_lengkap
print(b + ' ada di dalam' + nama_lengkap + '=' + str(status))

B = 'B'
status = B in nama_lengkap
print(B + ' ada di dalam' + nama_lengkap + '=' + str(status))

d = 'd'
status = d not in nama_lengkap
print(d + ' ada di dalam' + nama_lengkap + '=' + str(status))

# Mengulang String

print('wk'*10)
print(10*'wk')

# Indexing

print('index ke 0 pada' + nama_lengkap + '=' + nama_lengkap[0])
print('index ke 1 pada' + nama_lengkap + '=' + nama_lengkap[1])
print('index ke 2 dan 3 pada' + nama_lengkap + '=' + nama_lengkap[2:4]) #jika kita mau menampilkan index dari n1-n2 kita hareus + 1 n2 nya

# item paling kecil
print('plaing kecil = ' + min(nama_lengkap))
print('paling besar = ' + max(nama_lengkap))

ascii_code = ord(' ')
print('ascii code untuk spasi' + str(ascii_code))
data = 117
print('char untuk ascii 117 = ' + chr(data))

# 4. Operator dalam bentuk method

data = 'otong surotong patotong'
jumlah = data.count("o")
print('jumlah o pada ' + data + 'adalah'+ str(jumlah))