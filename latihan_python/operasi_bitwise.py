#operasi bitwise / binner

a = 9
b = 5

#bitwise or (|)
hasil = a | b
print('====bitwise or (|)====')
print("nilai :", a, ' , binary : ',format(a,'08b'))
print("nilai :", b, ' , binary : ',format(b,'08b'))
print('==========(|)==========')
print("nilai :", hasil, ' , binary : ',format(hasil,'08b'))

#bitwise and (&)
hasil = a & b
print('====bitwise and (&)====')
print("nilai :", a, ' , binary : ',format(a,'08b'))
print("nilai :", b, ' , binary : ',format(b,'08b'))
print('==========(&)==========')
print("nilai :", hasil, ' , binary : ',format(hasil,'08b'))

#bitwise xor (^)
hasil = a ^ b
print('====bitwise xor (^)====')
print("nilai :", a, ' , binary : ',format(a,'08b'))
print("nilai :", b, ' , binary : ',format(b,'08b'))
print('==========(^)==========')
print("nilai :", hasil, ' , binary : ',format(hasil,'08b'))

#bitwise not ()
hasil = ~a
print('====bitwise not (~)====')
print("nilai :", a, ' , binary : ',format(a,'08b'))
print('==========(~)==========')
print("nilai :", hasil, ' , binary : ',format(hasil,'08b'))

#ini kan kalo di miror misal 9 ke -10

#ini biar pas di moror misal dari 00001001 jadi 11110110

d = 0b00001001
e = 0b11111111
print('nilai :',e^d, ' binary : ', format(e^d,'08b'))