# kumpulan data / lsy

# kumpulan data angka
angka = [1,2,3,4,5]
print(angka)

# kum[upulan data string
string = ['a','b','c','d','e']
print(string)

# kumpulan data boolean
boolean = [True,False]
print(boolean)

# kumpulan data campuran
data_campuran = [1,'a',True]
print(data_campuran)

# alternative menggunakan list
data_list = list(range(0,10,2)) # range(start,stop,step)
print(data_list)

# membuat list menggunakan fot loop
data = [i for i in range(0,10)]
print(data)

# membuat list menggunakan for pake if
data = [i for i in range(0,10) if i != 5]
print(data)

data = [i for i in range(0,10) if i % 2 == 0]
print(data)

data = [i for i in range (0,10) if i % 2 != 0]
print(data) 