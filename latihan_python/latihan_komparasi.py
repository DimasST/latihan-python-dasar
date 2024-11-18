#latihan komparasi

#+++++3----10+++

inputUser = float(input("masukkan angka : "))

#validasi nilai < 3
isKurangDari = inputUser < 3
print('angka kurang dari 3 :', isKurangDari)

#validasi nilai > 10
isLebihDari = inputUser > 10
print('angkla lebih dari 10 :',isLebihDari)

isCorrect = isKurangDari or isLebihDari
print('angka kurang dari 3 atau lebih dari 10 :',isCorrect)

#----3++++10----
#kasus irisan

isKurangDari = inputUser < 10
print('angka kurang dari 10 :',isKurangDari)

isLebihDari = inputUser > 3
print('angka lebih dari 3 :',isLebihDari)

isCorrect = isKurangDari and isLebihDari
print('angka kurang dari 10 dan lebih dari 3 :',isCorrect)

#latihan komparasi

#1.----0++++5----8++++11---
#2.++++0----5++++8----11+++
print('No.1')
inputUser = float(input("masukkan angka : "))

isLebihDari = inputUser > 0
print('angka lebih dari 0 : ', isLebihDari)

isKurangDari = inputUser < 5
print('angka kurang dari 5 : ', isKurangDari)

isKurangDari1 = inputUser > 8
print('angka lebih dari 8 : ', isKurangDari1)

isLebihDari1 = inputUser < 11
print('angka kurang dari 11 : ', isLebihDari1)

isCorrect = isLebihDari or isKurangDari or isKurangDari1 or isLebihDari1
print('angka lebih dari 0 atau kurang dari 5 atau lebih dari 8 atau kurang dari 11 : ', isCorrect)

print('No.2')
inputUser = float(input("masukkan angka : "))

isKondisi1 = inputUser > 0
print("angka lebih dari 0 : ", isKondisi1)

isKondisi2 = inputUser < 5 and inputUser > 8
print("angka yang kurang dari 5 dan lebih dari 8 : ", isKondisi2)

isKondisi3 = inputUser > 11
print("angka lebih dari 11 : ", isKondisi3)

isCorrect = isKondisi1 or isKondisi2 or isKondisi3
print("angka lebih dari 0 atau kurang dari 5 dan kurang dari 8 atau kurang dari 11 : ", isCorrect)
