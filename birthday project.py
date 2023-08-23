#opening
print("Asikk skrg udah tanggal 2 September nih, katanya si ada yang ulang tahun siapa yaa??")

#nama
nama = input ("Nama kamu siapa sihh: ")
while nama!= "caca" :
    print("ihh nama kamu kan caca kok isi yang lain sihh")
    print(" ")
    nama = input ("Nama kamu siapa sihh: ")
    if nama == "caca":
        print("nah gitu dong yang benerr")
else:
    print("ciee, caca lagi ulang tahun ya katanya")
print(" ")

ultah_ke = input("Ultah yang ke berapa si: ")
while ultah_ke != "19":
    print("ihhh bukannya kamu ultah yang ke 19 tahun yaa")
    ultah_ke = input("Ultah yang ke berapa si: ")
if ultah_ke == "19":
    print("asikkk ada yang udah 19 tahun nih skrg")

#love dan ucapan
tinggi = 5
lebar = tinggi*2
simbol_1 = "C"
simbol_2 = "A"
print(" ")

#selamat
import time
for i in range (0,tinggi,2) :
    print (" "*(tinggi-(i))+simbol_1*i+ simbol_1*i + (" "*(tinggi-(i)))*2+simbol_1*i+ simbol_1*i)
    time.sleep(0.2)
for j in range(lebar,0,-2):
    print (" "*(lebar-j)+simbol_1*j+simbol_1*j)
    time.sleep(0.2)
print(" ")
print("♡"*6 +" selamat ".upper()+ "♡"*6)

#ulang
for i in range (0,tinggi,2) :
    print (" "*(tinggi-(i))+simbol_2*i+ simbol_2*i + (" "*(tinggi-(i)))*2+simbol_2*i+ simbol_2*i)
    time.sleep(0.2)
for j in range(lebar,0,-2):
    print (" "*(lebar-j)+simbol_2*j+simbol_2*j)
    time.sleep(0.2)
print(" ")
print("♡"*7 +" ulang ".upper()+ "♡"*7)

#tahun
for i in range (0,tinggi,2) :
    print (" "*(tinggi-(i))+simbol_1*i+ simbol_1*i + (" "*(tinggi-(i)))*2+simbol_1*i+ simbol_1*i)
    time.sleep(0.2)
for j in range(lebar,0,-2):
    print (" "*(lebar-j)+simbol_1*j+simbol_1*j)
    time.sleep(0.2)
print(" ")
print("♡"*7 +" tahun ".upper()+ "♡"*7)

for i in range (0,tinggi,2) :
    print (" "*(tinggi-(i))+simbol_2*i+ simbol_2*i + (" "*(tinggi-(i)))*2+simbol_2*i+ simbol_2*i)
    time.sleep(0.2)
for j in range(lebar,0,-2):
    print (" "*(lebar-j)+simbol_2*j+simbol_2*j)
    time.sleep(0.2)
print(" ")

#harapan dan doa
print("bentarr masih ada lagii")
penasaran = input("coba tebak ada apa lagi : ")
if penasaran == "gatau" or penasaran == "ga tau" :
    print("yeuuu masa gatau sihh kan ada yang belum aku ucapin ke kamu")
    print(" ")
    time.sleep(3)
else:
    print("akuu mau ucapin doa dan harapan buat kamuu")
    print(" ")
    time.sleep(2)

def doa():
    print("akuu mau ucapin doa dan harapan buat kamuu")
    time.sleep(3)
    print("nihh doa dan harapannya")
    time.sleep(2)
    print("semoga jadi anak yang baik, berguna buat orang sekitar, sayang sama keluarga")
    time.sleep(4)
    print("semoga cita-citanya tercapai dan semoga sukses dunia akhirat")
    time.sleep(3)
    print(" ")
    print("gatau ini kebetulan atau engga, tapi sadar ga si kamuu, ulang tahun kamu pas bgt sama tanggal jadian kitaa hehehehe")
    time.sleep(5)
    print("jadiiii aku sekalian aja dehh")
    time.sleep(2)
    print("makasihh udahhh selalu ngertiin akuu, makasih jugaa selama 6-7 bulan ini udah mau bertahan sama aku yang ga jelas ini")
    time.sleep(5)
    print("semoga kedepannya kita bisa makin mengerti satu sama lain, kurang-kurangin berantem yang ga perlu, sama jaga perasaan masing-masing")
doa()
for a in range(0,11,1):
    print("love you caca cantik".upper()+"♡")
    time.sleep(0.5)
    