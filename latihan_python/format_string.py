# format string

# contoh generic 
# string

nama = 'dimas'
format_str = f'hello {nama}'
print(format_str)

# angka
angka = 2005.5
format_str = f'Angka : {angka}'
print(format_str)

# boolean
boolean = True
format_str = f'Boolean : {boolean}'
print(format_str)

# bilangan bulat
angka = 2005
format_str = f'Angka : {angka:d}'
print(format_str)

# bilangan ribuan
angka = 20000000
format_str = f'Angka : {angka:,}' # menggunakan koma di belakang biar pas diprint ada koma di tiap 3 digit
print(format_str)

# bilangan desimal
angka = 2000.54321
format_str = f'Angka : {angka:.2f}' 
print(format_str)

# menggunakan leading zero
angka = 2000.54321
format_str = f'Angka : {angka:010.2f}'
print(format_str)

# menampilkan angka + / - 
angka_min = -10
angka_plus = 10
format_min = f'angka minus : {angka_min:+d}' # disini d buat validasi angka bulat
format_plus = f'angka plus : {angka_plus:+2f}' # bisa juga pake koma pake nf
print(angka_min)
print(angka_plus)

# format persen
angka = 0.045
format_persen = f'persen : {angka:.2%}'
print(format_persen)

# format angka lain (binary, Octagonal, hexagonal)
angka = 255
format_binary = f'binary : {bin(angka)}'
format_octagonal = f'octagonal : {oct(angka)}'
format_hexagonal = f'hexagonal : {hex(angka)}'

print(format_binary)
print(format_octagonal)
print(format_hexagonal)