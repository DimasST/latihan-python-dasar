# string wisth dan aligment

nama = 'dimas'
umur = 20
sepatu = 44
tinggi = 175

# string standar
print(5*'='+'data string'+5*'=')
data_string =f'nama : {nama}umur : {umur}sepatu : {sepatu}tinggi : {tinggi}'
print(data_string)

# string multiline menggunakan (\n)
print(5*'='+'data string multiline'+5*'=')
data_string =f'nama : {nama}\numur : {umur}\nsepatu : {sepatu}\ntinggi : {tinggi}'
print(data_string)

# string menggunakan triplets (''')
print(5*'='+'data string multiline triplets'+5*'=')
data_string = f'''
nama : {nama}
umur : {umur}
sepatu : {sepatu}
tinggi : {tinggi}
'''
print(data_string)

# mengatur lebar
print(5*'='+'data string multiline triplets'+5*'=')
data_string = f'''
nama   : {nama:>5}
umur   : {umur:>5}
sepatu : {sepatu:>5}
tinggi : {tinggi:>5}
'''
print(data_string)