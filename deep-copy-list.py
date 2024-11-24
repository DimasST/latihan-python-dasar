# deep copy list 
'''
kan kalo copy biasa yang di copy list nya 
kalo deep copy yang list dalem list nya ke copy juga jadi 
addres nya beda
'''
data_0 = [1,2,3]
data_1 = [4,5,6]
print(f'data 1 : {data_0}')
print(f'data 2 : {data_1}')
list_data = [data_0,data_1]
print(f'list data : {list_data}')
list_copy = list_data.copy()
print(f'data copy : {list_copy}')

print(f'addres data 1 : {hex(id(list_data[0]))}')
print(f'addres data 2 : {hex(id(list_copy[0]))}')
print(f'addres asli : {hex(id(list_data))}')
print(f'addres copy : {hex(id(list_copy))}')

# menggunakan deep copy biar pas kita copy list dalem list nya jadi addres nya beda

from copy import deepcopy

data_0 = [1,2,3]
data_1 = [4,5,6]
print(f'data 1 : {data_0}')
print(f'data 2 : {data_1}')
list_data = [data_0,data_1]
print(f'list data : {list_data}')
list_copy = deepcopy(list_data)
print(f'data copy : {list_copy}')

print(f'addres data 1 : {hex(id(list_data[0]))}')
print(f'addres data 2 : {hex(id(list_copy[0]))}')
print(f'addres asli : {hex(id(list_data))}')
print(f'addres copy : {hex(id(list_copy))}')

