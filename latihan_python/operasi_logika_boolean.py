#operasi logika
# not, or, and, xor

print('===not ')
a = True
c = not a

print("data a :", a)
print("======NOT")
print("data c :", c)

print('===OR')
a = False
b = False
c = a or b
print(a,'or',b,'=',c)
a = True
b = False
c = a or b
print(a,'or',b,'=',c)
a = False
b = True
c = a or b
print(a,'or',b,'=',c)
a = True
b = True
c = a or b
print(a,'or',b,'=',c)

print('===AND')
a = False
b = False
c = a and b
print(a,'and',b,'=',c)
a = True
b = False
c = a and b
print(a,'and',b,'=',c)
a = False
b = True
c = a and b
print(a,'and',b,'=',c)
a = True
b = True
c = a and b
print(a,'and',b,'=',c)

print('===XOR')
a = False
b = False
c = a or b
print(a,'xor',b,'=',c)
a = True
b = False
c = a ^ b
print(a,'xor',b,'=',c)
a = False
b = True
c = a ^ b
print(a,'xor',b,'=',c)
a = True
b = True
c = a ^ b
print(a,'xor',b,'=',c)
