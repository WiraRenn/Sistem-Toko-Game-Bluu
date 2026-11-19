from autentikasi import login, register
from admin import menu_admin
from pengguna import menu_user
from validasi import input_angka

def menu_utama():
    "Prosedur untuk menampilkan menu awal program."
    while True:
        print("-")
        print("       SISTEM TOKO GAME")
        print("-")
        print("1. Login")
        print("2. Register")
        print("3. Keluar")

        pilihan = input_angka("Pilih menu : ")

        if pilihan == 1:
            akun = login()

            if akun is not None:
                if akun["hak_akses"] == "Admin":
                    menu_admin()
                else:
                    menu_user(akun["username"])

        elif pilihan == 2:
            register()

        elif pilihan == 3:
            print("Terima kasih telah menggunakan Sistem Toko Game.")
            break

        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    menu_utama()