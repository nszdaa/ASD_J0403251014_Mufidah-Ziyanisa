Nama_File = "stok_barang.txt"

def baca_data(Nama_File):
    data_dict = {}  # inisialisasi dictionary kosong

    with open(Nama_File, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()  # hapus newline
            if not baris:
                continue

            Kode, NamaBarang, Stok = baris.split(",")
            data_dict[Kode] = {
                "Nama": NamaBarang,
                "Stok": int(Stok)
            }

    return data_dict

def tampilkan_data(data_dict):
    print("\n========= DAFTAR BARANG =========")
    print(f"{'Kode':<10} | {'Nama':<15} | {'Stok':>5}")
    print("-" * 36)

    for Kode in sorted(data_dict.keys()):
        NamaBarang = data_dict[Kode]["Nama"]
        Stok = data_dict[Kode]["Stok"]
        print(f"{Kode:<10} | {NamaBarang:<15} | {Stok:>5}")


def cari_data(data_dict):
    Kode_cari = input("Masukkan Kode barang: ").strip()

    if Kode_cari in data_dict:
        print("\n======= DATA DITEMUKAN =======")
        print(f"Kode : {Kode_cari}")
        print(f"Nama : {data_dict[Kode_cari]['Nama']}")
        print(f"Stok : {data_dict[Kode_cari]['Stok']}")
    else:
        print("Barang tidak ditemukan.")


def update_data(data_dict):
    Kode = input("Masukkan Kode barang: ").strip()

    if Kode not in data_dict:
        print("Kode tidak ditemukan.")
        return

    try:
        Stok_baru = int(input("Masukkan stok baru: "))
    except ValueError:
        print("Stok harus berupa angka.")
        return

    if Stok_baru < 0:
        print("Stok tidak boleh negatif.")
        return

    Stok_lama = data_dict[Kode]["Stok"]
    data_dict[Kode]["Stok"] = Stok_baru

    print(f"Stok berhasil diubah dari {Stok_lama} menjadi {Stok_baru}.")

def simpan_data(Nama_File, data_dict):
    with open(Nama_File, "w", encoding="utf-8") as file:
        for Kode in sorted(data_dict):
            Nama = data_dict[Kode]["Nama"]
            Stok = data_dict[Kode]["Stok"]
            file.write(f"{Kode},{Nama},{Stok}\n")


def main():
    data_barang = baca_data(Nama_File)

    while True:
        print("\n===== MENU STOK BARANG =====")
        print("1. Tampilkan semua barang")
        print("2. Cari barang berdasarkan kode")
        print("3. Update stok barang")
        print("4. Simpan ke file")
        print("0. Keluar")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tampilkan_data(data_barang)

        elif pilihan == "2":
            cari_data(data_barang)

        elif pilihan == "3":
            update_data(data_barang)

        elif pilihan == "4":
            simpan_data(Nama_File, data_barang)
            print("Data berhasil disimpan.")

        elif pilihan == "0":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid.")


# ---------- Eksekusi Program ----------
if __name__ == "__main__":
    main()
