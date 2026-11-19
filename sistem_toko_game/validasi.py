def input_teks(pesan):
    "Meminta input teks yang tidak boleh kosong."
    while True:
        try:
            nilai = input(pesan).strip()

            if nilai == "":
                raise ValueError("Input tidak boleh kosong!")

            return nilai

        except ValueError as error:
            print("Kesalahan:", error)


def input_angka(pesan, minimum=None):
    "Meminta input angka bulat dan memeriksa nilai minimumnya."
    while True:
        try:
            angka = int(input(pesan))

            if minimum is not None and angka < minimum:
                raise ValueError("Angka minimal adalah " + str(minimum) + ".")

            return angka

        except ValueError:
            print("Input harus berupa angka bulat yang valid!")
            if minimum is not None:
                print("Nilai minimal:", minimum)


def konfirmasi(pesan):
    "Meminta konfirmasi Ya atau Tidak menggunakan try-except-finally."
    while True:
        try:
            jawaban = input(pesan + " (ya/tidak): ").lower().strip()

            if jawaban == "ya":
                return True
            elif jawaban == "tidak":
                return False
            else:
                raise ValueError("Masukkan hanya ya atau tidak !")

        except ValueError as error:
            print("Kesalahan:", error)

        finally:
            print("Pemeriksaan konfirmasi selesai.")