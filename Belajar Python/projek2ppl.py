#fungsi garis
def garis1():
    print("==========")

def garis2():
    print("----------")

# Perpus kosong untuk menyimpan buku
buku = []

# fungsi show buku (perlihatkan buku)
def show_buku():
    if len(buku) <= 0:
        print ("Buku Kosong Mas!")
        garis1()
    else:
        for indeks in range(len(buku)):
            garis1()
            print ("[{}]] {}".format (indeks,buku [indeks]))
            garis1()
# fungsi edit buku
def edit_buku():
    show_buku()
    indeks = int(input("Inputkan ID BUKU : "))
    if indeks > len(buku):
        print("ID SALAH")
        garis2()
    else:
            judul_baru = input("Judul Baru : ")
            buku[indeks] = judul_baru
            garis2()
            print("Buku Berhasil diRubah")
            show_buku()
            garis1()
# fungsi insert buku
def insert_buku():
    garis1()
    buku_baru = input("Judul Buku : ")
    buku.append(buku_baru)
    garis2()
    print("Buku Berhasil diTambah !!!")
    garis1()
#fungsi delete
def delete_buku():
    show_buku()
    indeks = int(input("Inputkan ID BUKU : "))
    if indeks > len(buku):
        print ("ID SALAH")
    else:
        buku.remove(buku[indeks])
        garis1()
        print ("Buku Berhasil diHapus ")
        garis2()

# Menu untuk tampilan perpus
def show_menu():
    print ("\n")
    print("-Selamat datang di Perpus-")
    print("1. Show Buku")
    print("2. Insert Buku")
    print("3. Edit Buku")
    print("4. Delete Buku")
    print("5. Keluar")

    menu = int(input("Pilih Menu : > "))

    if menu == 1:
        show_buku()
    elif menu == 2:
        insert_buku()
    elif menu == 3:
        edit_buku()
    elif menu == 4:
        delete_buku()
    elif menu == 5:
        exit()
    else:
        print ("Upss Salahhh")

# tampilkan Menu
if __name__ == "__main__":
    while True:
        show_menu()
