print ("--------------SEWA MOBIL MURAH--------------")
print ("----MELAYANI SEWA MOBIL SESUAI KEBUTUHAN----")

nama = input("masukkan nama lengkap anda :")
print ("nama lengkap :  " ,nama)
alamat = input("masukkan alamat anda : ")
print ("nama lengkap :  " ,nama)
print ("alamat :" ,alamat)
usia = int (input("masukkan usia anda :"))

if usia > 20:
        print ("pilih jenis mobil yang akan anda sewa :" )
elif usia < 20 :
    breakpoint()
    print ("maaf hanya usia di atas 20 tahun yang di perbolehkan menyewa mobil....:(")
            

mobil = ["avanza" , "grand livina" , "mobilio" , "brio" , "ayla" , "agya" , "pickup + supir"]

for list in nama:
    print("daftar mobil :")
    print("-----1. ", mobil[0],)
    print("-----2. ", mobil[1],)
    print("-----3. ", mobil[2],)
    print("-----4. ", mobil[3],)
    print("-----5. ", mobil[4],)
    print("-----6. ", mobil[5],)
    print("-----7. ", mobil[6],)
    break   
harga = [
    "avanza        : Rp,150,000" ,
    "grand livina  : Rp,200,000" ,
    "mobilio       : Rp,250,000" ,
    "brio          : Rp,100,000" ,
    "ayla          : Rp,100,000" ,
    "agya          : Rp,100,000" ,
    "pickup        : Rp,150,000" ,]
for list in harga:
    print(" daftar harga")
    print("-----1. ", harga[0],)
    print("-----2. ", harga[1],)
    print("-----3. ", harga[2],)
    print("-----4. ", harga[3],)
    print("-----5. ", harga[4],)
    print("-----6. ", harga[5],)
    print("-----7. ", harga[6],)
    break
yakin = (input("apakah anda ingin melanjutkan pesanan (iya / tidak) : ")) 
if yakin == "iya":
    print ("silahkan pilih jenis dan berapa lama anda akan memesan :")
else :
    breakpoint()
    print ("terimaksih telah mengunjungi sewa mobil kami")
    

jenis = int (input("silahkan pilih jenis mobil yang ingin anda sewa (pilih nomer) :"))
waktu = int (input("silahkan isi berapa lama anda akan menyewa (hari)"))

if jenis == 1 :
    biaya1 = waktu*150000
    print ("------PESANAN SEWA MOBIL------")
    print ("nama lengkap      :" ,nama)
    print ("alamat            :" ,alamat)
    print ("usia              :" , usia)
    print ("sewa mobil jenis  :" , mobil [0])
    print ("waktu/durasi sewa :" , waktu , "hari")
    print ("biaya sewa Rp     :" , biaya1)
    print ("---TERIMA KASIH---")
elif jenis == 2 :
    biaya2 = waktu*200000
    print ("------PESANAN SEWA MOBIL------")
    print ("nama lengkap      :" ,nama)
    print ("alamat            :" ,alamat)
    print ("usia              :" , usia)
    print ("sewa mobil jenis  :" , mobil [1])
    print ("waktu/durasi sewa :" , waktu , "hari")
    print ("biaya sewa Rp     :" , biaya2)
    print ("---TERIMA KASIH---")
elif jenis == 3 :
    biaya3 = waktu*250000
    print ("------PESANAN SEWA MOBIL------")
    print ("nama lengkap      :" ,nama)
    print ("alamat            :" ,alamat)
    print ("usia              :" , usia)
    print ("sewa mobil jenis  :" , mobil [2])
    print ("waktu/durasi sewa :" , waktu , "hari")
    print ("biaya sewa Rp     :" , biaya3)
    print ("---TERIMA KASIH---")
elif jenis == 4 :
    biaya4 = waktu*100000
    print ("------PESANAN SEWA MOBIL------")
    print ("nama lengkap      :" ,nama)
    print ("alamat            :" ,alamat)
    print ("usia              :" , usia)
    print ("sewa mobil jenis  :" , mobil [3])
    print ("waktu/durasi sewa :" , waktu , "hari")
    print ("biaya sewa Rp     :" , biaya4)
    print ("---TERIMA KASIH---")
elif jenis == 5 :
    biaya5 = waktu*100000
    print ("------PESANAN SEWA MOBIL------")
    print ("nama lengkap      :" , nama)
    print ("alamat            :" , alamat)
    print ("usia              :" , usia)
    print ("sewa mobil jenis  :" , mobil [4])
    print ("waktu/durasi sewa :" , waktu , "hari")
    print ("biaya sewa Rp     :" , biaya5)
    print ("---TERIMA KASIH---")
elif jenis == 6 :
    biaya6 = waktu*100000
    print ("------PESANAN SEWA MOBIL------")
    print ("nama lengkap      :" , nama)
    print ("alamat            :" , alamat)
    print ("usia              :" , usia)
    print ("sewa mobil jenis  :" , mobil [5])
    print ("waktu/durasi sewa :" , waktu , "hari")
    print ("biaya sewa Rp     :" , biaya6)
    print ("---TERIMA KASIH---")
elif jenis == 2 :
    biaya7 = waktu*150000
    print ("------PESANAN SEWA MOBIL------")
    print ("nama lengkap      :" ,nama)
    print ("alamat            :" ,alamat)
    print ("usia              :" , usia)
    print ("sewa mobil jenis  :" , mobil [6])
    print ("waktu/durasi sewa :" , waktu , "hari")
    print ("biaya sewa Rp     :" , biaya7)
    print ("---------TERIMA KASIH---------")
