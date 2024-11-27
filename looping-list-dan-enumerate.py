# looping list

# menggunakan for loop

angka = [1,3,2,5,6]

print('menggunakan for loop')

for i in angka:
    print(f'angka : {i}')

# menggunakan for loop dan range

print('menggunakan for loop dan range')

for i in range(len(angka)):
    print(f'angka : {angka[i]}')

# menggunakan while loop

print('menggunakan while loop')

i = 0

while i < len(angka):
    print(f'angka : {angka[i]}')
    i += 1
    
# menggunakan list comprehenseion
print('menggunakan list comprehension')
data = ['dimas',1,2,3,2,3]

[print(f'data : {i}')for i in data]

angka = [1,23,4,2,1]
angka_kuadrat = [i**2 for i in angka]
print(angka_kuadrat)

# menggunakan enumerate 
# mengambil nilai data dan index

print('menggunakan enumerate')

data = ['dimas',1,2,3,2,3]

for index,data in enumerate(data):
    print(f'index : {index} data : {data}')