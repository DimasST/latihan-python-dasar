# latihan date and time

import datetime as dt

print('Silahkan masukan \ntanggal \nbulan \ntahun lahir anda')
tanggal = int(input('Tanggal : '))
bulan = int(input('Bulan : '))
tahun = int(input('Tahun : '))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f'tanggal lahir anda adalah : {tanggal_lahir}')

hari_ini = dt.date.today()
print(f'hari ini : {hari_ini}')
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365) // 30

print(f'Hari ini adalah : {hari_ini}')
print(f'Umur anda adalah : {umur_tahun} tahun {umur_bulan_sisa} bulan')
print(f'Anda lahir hari : {tanggal_lahir:%A}')