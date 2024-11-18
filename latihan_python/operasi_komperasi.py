#operasi komperasi

# > < <= >= == != is is not
a = 5
b = 3

print('=== lebih besar dari > ')
hasil = a > 3
print(a, ">", 3 , "=", hasil)
hasil = b > 3
print(b, ">", 3 , "=", hasil)
hasil = b > 3
print(b, ">", 3 , "=", hasil)

print('=== kurang dari <  ')
hasil = a < 3
print(a, "<", 3 , "=", hasil)
hasil = b < 3
print(b, "<", 3 , "=", hasil)
hasil = b < 3
print(b, "<", 3 , "=", hasil)

print('=== lebih dari sama dengan >= ')
hasil = a >= 3
print(a, ">=", 3 , "=", hasil)
hasil = b >= 3
print(b, ">=", 3 , "=", hasil)
hasil = b >= 3
print(b, ">=", 3 , "=", hasil)

print('=== kurang dari sama dengan <= ')
hasil = a <= 3
print(a, "<=", 3 , "=", hasil)
hasil = b <= 3
print(b, "<=", 3 , "=", hasil)
hasil = b <= 3
print(b, "<=", 3 , "=", hasil)

print('=== sama dengan == ')
hasil = a == 3
print(a, "==", 3 , "=", hasil)
hasil = b == 3
print(b, "==", 3 , "=", hasil)
hasil = b == 3
print(b, "==", 3 , "=", hasil)

print('=== tidak sama dengan = ')
hasil = a != 3
print(a, "!=", 3 , "=", hasil)
hasil = b != 3
print(b, "!=", 3 , "=", hasil)
hasil = b != 3
print(b, "!=", 3 , "=", hasil)

#komparasi is dan is not
#komparasi is dan is not dikhususkan untuk objek identitiy atau untuk membandingkan variabel/objek identity
print('===komparasi is ')
x = 5 #ini adalah assigment object
y = 5

print("nilai x :",x,hex(id(x)))
print("nilai y :",y,hex(id(y)))
hasil = x is y
print('x is y : ' , hasil)

print('===komparasi is not ')
x = 5 #ini adalah assigment object
y = 5

print("nilai x :",x,hex(id(x)))
print("nilai y :",y,hex(id(y)))
hasil = x is not y
print('x is y : ' , hasil)

