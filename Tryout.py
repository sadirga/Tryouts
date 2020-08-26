## SOAL PERTAMA 
# BUATLAH PROGRAM MENGGUNAKAN IF ELSE (conditional) untuk menentukan
# apakah suatu bilangan tergolong bilangan PRIMA atau BUKAN
# Bilangan PRIMA: BILANGAN YANG HANYA HABUS DIBAGI OLEH 1 DAN BILANGAN ITU SENDIRI

# num = int(input('angka: '))

# for i in range(num):
#     if  i>1 and num%i==0 :
#         print(num,'bukan bilangan prima')
#         break
# else:
#     if num< 2:
#         print(num,'bukan bilangan prima')
#     else:
#         print(num,'bilangan prima')



# SOAL KEDUA
# Buatlah function untuk mengganti/duplikasi built-in function REPLACE() pada data string!
# Output yang diharapkan: 
# data = 'Visualisasi' 
# ganti(data, 'V', 'P') =====> keluarnya = 'Pisualisasi'

# def Riples(kata,kar_ori='a',kar_pengganti='i'): # Buat nama function dan 2 parameter
#     baru = ''                                   # Buat variable string kosong dengan nama baru
#     for i in kata:                              # loop setiap elemen kata
#         if i == kar_ori:                        # Jika elemen i sama dengan value parameter pertama kar_ori
#             i = kar_pengganti                   # Maka elemen i tersebut diganti dengan value parameter kedua kar_pengganti
#         baru += i                               # Setiap looping elemen i berjalan, variable baru akan ditambah elemen i
#     return baru

# data = 'Visualisasi'
# print(Riples(data,'i','u'))

def Riples(kata,kar_ori='a',kar_pengganti='i'): 
    baru = ''                                   
    for i in kata:                              
        if i == kar_ori:                        
            i = kar_pengganti                   
        baru += i                               
    return baru

data = 'Visualisasi'
print(Riples(data))

# def ganti(string1,awal,pengganti)

# SOAL KETIGA (TAKE HOME)
## Buat function untuk membalikkan posisi list
# data = [['a', 'b'], ['e', 'f' ]]
# data = [['a', 'b'], 
#         ['e', 'f' ]]
# menjadi/output yang diharapkan:
# data_mutar = [['e', 'a'], ['f', 'b' ]]
# data_mutar = [['e', 'a'], 
#             ['f', 'b' ]]

def putarData(data):                         # Buat nama function dan parameter
    baru =[]                                 # Buat variable list kosong dengan nama baru
    for i in range(len(data)-1):             # loop i sepanjang len data -1 agar hanya merujuk ke data index 0
        data1=[data[i-1][i],data[i][i]]      # store di variable list baru hasil dari slicing data[i-1](merujuk ke list index 1)[i]merujuk ke elemen pertama di list index 1
        baru.append(data1)                   # lalu hasilnya di append atau disisipkan ke variable baru
    for j in range(1,len(data)):             # kemudian loop lagi tapi hanya merujuk k 
        baru.append([data[j][j],data[i][j]])    
    print(baru)
            
data = [['a', 'b'], ['e', 'f' ]]
putarData(data)

# Mas Kim Answer
# def putarList(yourList):
#     data_mutar = [[],[]]
#     for i in range(len(yourList)):
#         for j in range(len(yourList)):
#             data_mutar[i].append(yourList[(len(yourList])

