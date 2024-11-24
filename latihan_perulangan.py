# latihan perulangan membuat segitiga

# 1.Menggunakan for
sisi = 11
print('awal for')
count = 1
for i in range(sisi):
    print('+'*count)
    count += 1
print('akhir for')

# 2.Menggunakan while
print('awal while')
count = 1
while True:
    print('+'*count)
    count += 1
    
    if count > sisi:
        break
print('akhir while')

# 3.hanya ganjil aja
print('awal while')
count = 1
while True:
    if (count%2):
        print("+"*count)
        count += 1
    else:
        count += 1
        continue
    if count > sisi:
        break
print('akhir while')

# 4.membuat segitiga sama kaki

print('awal while')
count = 1
spasi = int(sisi/2)
while True:
    if (count%2):
        print(' '*spasi, '+'*count)
        spasi -= 1
        count += 1 
    else:
        count += 1
        continue
    if count > sisi:
        break
while True:
    if (count%2):
        spasi += 1
        print(' '*spasi, '+'*count)
        count -= 1
    else:
        count -= 1
        continue
    if count < 1:
        break
# Tugas membuat ketupat 
