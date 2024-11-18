#penggunaan string 


#1. Cara membuat string
print("=== penggunaan string ===")
#menggunakan single qoute
print('halo dunia')
#menggunakan double qoute
print("halo dunia")

print("Sekarang hari jum'at")
print('"Halo apa kabar?"')
print("'Halo apa kabar?'")

#2. Menggunakan tanda \
print('sekarang hari jum\'at')

#backslash
print('c:\\user\\budi') #menggunakan tanda \ 2x biar kebca string yang satu laginya

#tab
print('ucup \t ucup \t ucup , sekarang jadi jauh jauhan ')

#backspace
print('ucup \b ucup \b ucup , sekarang jadi deketan ')

#newline
print('ini baris pertama \n ini baris kedua') #CR -> carriage return biasa di pake di linux macos / yang uniqe
print('ini baris pertama \r ini baris kedua') #LF -> line feed di pake di sistem operasi yang udah lawas
print('ini baris pertama \r\n ini baris kedua') #CRLF -> carriage return line feed biasa di pake di sistem windows

#3. string literal / raw
print('c:\new folder') # akan salah path nya 

#menggunakan argumen raw string
print(r'c:\new folder')

#multiline literal string
print("""
ini baris pertama
ini baris kedua
ini baris ketiga
""") #seperti komen ini bisa menggangap semua yang di dalam jadi string mau itu spasi sekalipun

#multiline literal string dan raw string
print(r"""
c:\new folder
ini baris kedua
ini baris ketiga
""")