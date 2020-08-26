# SOAL PERTAMA
# Buat function untuk mendapatkan domain dari alamat user
# alamat = 'alamatku@gmail.com'
# emailku = 'belajar@yahoo.com'
# domain(alamat) -----> output: 'gmail.com'
# domain(emailku) -----> output: 'yahoo.com'

def alamat_email(email):        # Buat nama function dan parameter
    email = email.split("@")    # split parameter email dengan separator "@" agar domain email dipisah dari usernamenya
    return email[-1]            # lalu ambil value menggunakan method slicing dan negative indexing

email = "belajar@gmail.com"
print(alamat_email(email))

# One Liner
# def alamat_email(email):
#     return email.split("@")[-1]

# Yosafat answer
# def domain(email):
#     index = email.index('@')
#     domain = email[index+1:]
#     return domain

#_______________________________________________________________________________________________________________________________________________________________

# SOAL KEDUA
# Buat function untuk menghitung teks tertentu dalam suatu string
# komentar = 'Saya sedang belajar Data Science'
# HitungTeks('belajar', komentar)   --> Ada 1 kata 'belajar'

def hitung_kata(teks,kata):             # Buat nama function dan 2 parameter
    count = 0                           # Siapkan variable dengan value 0 type int
    for i in teks.split(" "):           # loop setiap elemen di dalam teks yang sudah menjadi list karena displit dengan separator " "
        if i == kata:                   # Masuk ke kondisi jika ditemukan elemen di dalam list teks sama dengan parameter kata
            count+=1                    # Maka, variable count ditambah 1 nilainya
    print(f"ada {count} kata '{kata}'")
 
komentar = 'Saya sedang saat saat belajar Data Science'
hitung_kata(komentar,'saat')

#_______________________________________________________________________________________________________________________________________________________________

# SOAL KETIGA
# Gunakan lambda expressions dan filter() function untuk memfilter nama-nama orang yang diawali huruf 'B'
# nama = ['Andi', 'Caca', 'Budi', Dody','Bambang','Edi','Ari','Bintang']
# output = ['Budi','Bambang','Bintang']

list_nama = ['Andi', 'CacaB', 'Budi', 'Dody','Bambang','Edi','Ari','Bintang'] 
cari_nama = list(filter(lambda x : x.startswith("B") ,list_nama)) 
print(cari_nama)

list_nama = ['Andi', 'CacaB', 'Budi', 'Dody','Bambang','Edi','Ari','Bintang'] 
cari_nama = list(filter(lambda x : "B" in x[0] ,list_nama)) 
print(cari_nama)


#_______________________________________________________________________________________________________________________________________________________________

# SOAL KEEMPAT
# Buat function untuk menghitung gaji bersih karyawan-karyawan setelah dikurangi pajak 5 persen
# Buat 2 versi: 1) menggunakan function biasa, 2) menggunakan lambda function
# gaji = [5, 8, 9, 10, 20, 6, 5]
# output = [4.75, 7.6, 8.55, 9.5, 19.0, 5.7, 4.75]

# Versi 1 Function

def net_gaji(list_gaji):            # buat function dengan parameternya
    list_net = []                   # siapkan variable list kosong
    for i in list_gaji:             # loop setiap elemen di list_gaji
        list_net.append(i-(i*0.05)) # setiap elemen akan melewati perhitungan dan hasilnya akan di append k list kosong yang kita buat sebelumnya
    return list_net
         
gaji = [5, 8, 9, 10, 20, 6, 5]
print(net_gaji(gaji))

# Versi 2 Lambda Expression

gaji = [5, 8, 9, 10, 20, 6, 5]
gaji_net = list(map(lambda net:net-(net*0.05),gaji))

print(gaji_net)

#_______________________________________________________________________________________________________________________________________________________________

# SOAL KELIMA (BONUS)
# Buat function untuk membuat list angka ganjil dalam range tertentu
# tapi bergantian ganjil positif dan ganjil negatif
# Contoh: ganjilMix(20) ---> output: [1, -3, 5, -7, 9, -11, 13, -15, 17, -19]

def ganjilplusminus(num):               # buat function dengan parameternya
    list_num=[]                         # siapkan variable list kosong
    for i in range(1,num,2):            # loop i dengan range dimulai dari 1 , diakhiri num, increment nya 2
        list_num.append(i)              # lalu hasil loop i dimasukkan ke variable list kosong tadi
    for j in range(1,len(list_num),2):  # lalu list_num di loop lagi dengan range dimulai dari 1 (agar iterasi dimulai dari elemen kedua), berakhir di panjang elemen list_num increment juga 2
        list_num[j] *= -1               # lalu setiap elemen list num dengan index j (dimana index j akan berjalan melongkapi 1 elemen) akan di kalikan minus 1
    return list_num                     
print(ganjilplusminus(30))


# Ezra Answer
def ganjilMix(rangeStop):
    return [x if i % 2 == 0 else -x for i, x in zip(range(len(range(1,rangeStop,2))), range(1, rangeStop, 2))]

print(ganjilMix(30))
