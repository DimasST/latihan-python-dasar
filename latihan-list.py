# latihan list 

list_buku = []

while True:
    print('\n Masukan data buku')
    
    judul = input('Masukan judul buku \t: ')
    penulis = input('Masukan penulis buku \t: ')
    
    buku_baru = [judul,penulis]
    list_buku.append(buku_baru)
    
    print('\n\n,','='*10,'data buku', '='*10)
    for index,buku in enumerate(list_buku):
        print(f'{index+1}, | {buku[0]} | {buku[1]}')
        
    print('\n\n','='*20)
    isLanjut = input('apakah sudah selesai ? (y/n) \t: ')
    if isLanjut == 'n':
        break
print('program selesai')