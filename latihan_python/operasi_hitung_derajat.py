#menghitung konversi derajat

celcius = float(input("masukkan derajat celcius : "))

print("data suhu :", celcius,"celcius")

#konversi ke fahrenheit
fahrenheit = (celcius * 9/5) + 32
print("data suhu dalam fahrenheit:", fahrenheit,"fahrenheit")

#konersi ke reamur
reamur = (4/5) * celcius
print("data suhu dalam reamur : ", reamur,"reamur" )

#konersi ke kelvin
kelvin = celcius + 273
print("data suhu dalam kelvin : ", kelvin,"kelvin" )

#tugas

#merubah fahrenhit ke kelvin

fahrenheit = float(input("masukan derajat dalam fahrenheit :"))
kelvin = ((5/9) * (fahrenheit - 32)) + 273
print("data dalam kelvin : ",kelvin)

#merubah kelvin ke fahrenheit

kelvin = float(input("masukan derjat dalam kelvin :"))
celcius = kelvin - 273
fahrenheit = ((9/5) * celcius) + 32
print ('derajat dalam fahrenheit :', fahrenheit)