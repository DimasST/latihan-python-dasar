# operasi dan manipulasi string menggunakan method

# merubah case dari string

# merubah semua string ke lower case

nama = 'Dimas Saktiawan'
print("normal : " + nama)
nama = nama.lower()
print("lower : " + nama)

# merubah semua string ke upper case
nama = 'dimas saktiawan'
print('normal : ' + nama)
nama = nama.upper()
print('upper : ' + nama)

## pengecekan dengan isX method

# contoh pengecekan lower case
nama = 'dimas saktiawan'
nama_lower = nama.islower()
print (nama + 'cek lower : ' + str(nama_lower))

# pengecekkan upper case
nama = 'DIMAS SAKTIAWAN'
nama_upper = nama.isupper()
print (nama + 'cek upper : ' + str(nama_upper))

# isalpha() <-- untuk mengecek semua karakter dalam string adalah huruf
# isalnum() <-- untuk mengecek semua karakter dalam string adalah huruf atau angka
# isdecimal() <-- untuk mengecek semua karakter dalam string adalah angka
# isspace() <-- untuk mengecek semua karakter dalam string adalah spasi
# istitle() <-- untuk mengecek semua kata dalam string adalah capitalize
# isnumeric() <-- untuk mengecek semua karakter dalam string adalah angka
# isdigit() <-- untuk mengecek semua karakter dalam string adalah angka

# istitle

judul = 'Hujan Di Bulan Juni'
cek_judul = judul.istitle(  )
print(judul + 'title : ' + str(cek_judul))

## mengecek komoponen startswith dan endswith

cek_start = 'Hujan Di Bulan Juni'.startswith('Hujan')
print(judul + 'start : ' + str(cek_start))

cek_end = 'Hujan Di Bulan Juni'.endswith('Juni')
print(judul + 'end : ' + str(cek_end))

## penggabungan komponen join() dan split()

pisah = ['aku', 'sayang', 'kamu']
gabungan = ' '.join(pisah)
print(pisah)
print(gabungan)

pisah = ['aku', 'sayang', 'kamu']
gabungan = 'ehm'.join(pisah)
print(pisah)
print(gabungan)

kata = 'aku sayang kamu'
pisah = kata.split()
print(kata)
print(pisah)

## alokasi karakter rjust() ljust() center()

kanan = 'kanan'.rjust(10)
print("'"+kanan+"'")

kiri = 'kiri'.ljust(10)
print("'"+kiri+"'")

tengah = 'tengah'.center(10,'-')
print("'"+tengah+"'")

# -> kebalikannya strip

kanan = kanan.strip()
print("'"+kanan+"'")