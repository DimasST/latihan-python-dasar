# mengcopy list

a = ['dimas','otong','koli']
print(f'data a : {a}')
b = a
print(f'data b : {b}')

b[1] = 'ucup'
print(f'data b setelah diubah : \n{b}')
print(f'data a : \n{a}')

# cara mengcopy list biar tidak sama addres nya
c = a.copy()
print(f'data c : \n{c}')

print(f'addres data a : {hex(id(a))}')
print(f'addres data a : {hex(id(b))}')
print(f'addres data a : {hex(id(c))}')

print(f'data a : \n{a}')
print(f'data a : \n{b}')
print(f'data a : \n{c}')

print('kita rubah data ke 0')
c[0] = 'dimis'
print(f'data a : \n{a}')
print(f'data a : \n{b}')
print(f'data a : \n{c}')

print('kita rubah data ke 1')
b[1] = 'icip'
print(f'data a : \n{a}')
print(f'data a : \n{b}')
print(f'data a : \n{c}')