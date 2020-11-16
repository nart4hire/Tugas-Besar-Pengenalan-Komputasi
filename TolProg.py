# Fungsi untuk mendapatkan jenis kendaraan dari input pengguna/sistem.
# Kita asumsikan input pertama hanya terdapat dua jawaban "Y" atau "N"(boolean)
# Basis asumsi ini adalah jikalau input berasal dari manusia, maka bisa diberikan dua pilihan saja
# alias tidak diberi opsi selain "Y" atau "N"
# Asumsi untuk input kedua, adalah input device hanya berupa input angka 2-5 untuk input dari manusia.
# (Gandar adalah pasang roda pada truk)
def get_vtype():
    if input("Apakah kendaraan adalah truk?(Y/N) ") == "Y":
        vt = int(input("Jumlah gandar pada truk: "))
    else:
        vt = int(1)
    return vt


# Fungsi untuk memasukkan ruas tol, gerbang masuk, dan gerbang keluar.
# Karena fungsi ini akan diloop sampai dapat, maka tidak apa-apa kalau salah memasukkan data
# Data yang dapat dimasukkan: Nama ruas tol, Gerbang masuk, dan Gerbang keluar dengan
# kapitalisasi bebas tetapi harus sama dengan ejaan di "index.txt"
def get_loc():
    ruas = input("Ruas Tol: ").upper()
    gb_awal = "GT_" + input("Gerbang Masuk: ").upper()
    gb_akhir = input("Gerbang Keluar: ").upper()
    loc = [ruas, gb_awal, gb_akhir]
    return loc


# fungsi untuk mencari substring dalam string, berguna dalam mencari harga dari text file yang besar
def find_str(main, sub):
    found = main.find(sub)
    if found != -1:
        return True
    else:
        return False


# Argumen pembuka untuk menentukkan jenis kendaraan dan membuka "index.txt" dan memisahkannya di "###"
v_type = get_vtype()
index = open("index.txt", "r")
index = index.read().split("###")
valid = False  # variabel boolean yang dipakai untuk mematahkan loop dibawah

# loop untuk menentukkan harga dari perjalanan yang telah ditempuh
# fungsi get_loc() akan terus diloop sampai dapat input yang sesuai
while True:
    ticket = get_loc()
    for item in index:  # menemukan ruas tol yang dilalui kendaraan
        if find_str(item, ticket[0]) is True:
            start = item.split("---")  # data per gerbang dimasukkan ke variabel "start"
            break  # data per gerbang pada file text dipisah oleh "---" yang displit disini.

    try:  # try dan except untuk typo dalam salah input
        for line in start[1:]:  # menemukan gerbang yang dimasuki oleh pengendara
            if find_str(line, ticket[1]) is True:
                finish = line.split("\n")  # data per gerbang keluar dimasukkan ke variabel "finish"
                break  # data per gerbang dipisah dengan line baru sehingga displit memakai "\n"
    except NameError:
        pass

    try:  # try dan except untuk typo dalam salah input
        for line in finish[1:]:  # Menemukan gerbang keluar pengendara
            if find_str(line, ticket[2]) is True:
                pricing = line.split(" ")  # data harga per jenis kendaraan dimasukkan ke variabel "pricing'
                valid = True  # harga dipisahkan memakai spasi sehingga displit memakai " "
                break  # valid adalah benar karena sudah benar jika sudah memilikki harga.
    except NameError:
        pass

    if valid is True:
        break  # mematahkan loop jika karcis valid
    else:
        print("Tiket yang anda masukkan tidak valid!")  # prompt memberi tahu user bahwa input salah

price = float(pricing[v_type]) * 1000
if input("Apakah kartu e-toll hilang?(Y/N) ") == "Y":  # tarif tambahan jika kartu e-toll hilang
    price *= 2  # sesuai peraturan yang berlaku. (dua kali harga)

# print karcis keluar
print("---RUAS TOL " + ticket[0] + "---\n\nJenis Kendaraan: " + str(v_type) + "\nGerbang Masuk  : " + ticket[1])
print("Gerbang Keluar : " + ticket[2] + "\nHarga          : Rp" + str(price) + "0\n\n---SELAMAT JALAN---")

# Catatan tambahan untuk format file index.txt:
#
# NAMA_RUAS_TOL ## cth: TANGERANG-MERAK, JORR_02
# ---GT_NAMA_GERBANG_MASUK
# NAMA_GERBANG_KELUAR 1.00 2.00 3.00 4.00 5.00 (angka merupakan harga untuk jenis kendaraan 1, 2, 3, 4, 5)
#
# diperlukan pembeda diantara nama gerbang masuk dan keluar sehingga diberi "GT_" untuk gerbang tol masuk
