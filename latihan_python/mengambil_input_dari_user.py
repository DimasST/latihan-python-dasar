#kalo masukin input otomatis jadi type string
data = input("masukkan data : ")
print('data :', data, 'type :', type(data))
#kita casting dlu biar type inputan nya bisa berubah jadi integer dan float
angka = int(input("masukkan angka : "))
print('angka :', angka, 'type :', type(angka))
angka = float(input("masukkan angka : "))
print('angka :', angka, 'type :', type(angka))
#casting inputan jadi nilai boolean
angka = bool(int(input("masukkan angka : ")))
print('angka :', angka, 'type :', type(angka))