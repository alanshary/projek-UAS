class Data:
    """Class untuk menyimpan data nilai UAS."""
    def __init__(self, nama, nim, nilai_uas):
        self.nama = nama
        self.nim = nim
        self.nilai_uas = nilai_uas


class View:
    """Class untuk input dan output dari pengguna."""
    @staticmethod
    def input_data():
        nama = input("Masukkan nama: ").strip()
        nim = input("Masukkan NIM: ").strip()
        nilai_uas = input("Masukkan nilai UAS: ").strip()
        return Data(nama, nim, nilai_uas)

    @staticmethod
    def tampilkan_data(data_list):
        # Menyiapkan data untuk tabel
        tabel_data = [["No", "Nama", "NIM", "Nilai UAS"]]
        for i, data in enumerate(data_list, start=1):
            tabel_data.append([i, data.nama, data.nim, data.nilai_uas])
        
        # Menampilkan tabel
        tampilkan_tabel(tabel_data)


def tampilkan_tabel(data):
    """Fungsi untuk menampilkan tabel."""
    # Menentukan lebar kolom
    col_widths = [max(len(str(item)) for item in column) for column in zip(*data)]

    # Mencetak header tabel
    header = " | ".join(f"{str(data[0][i]):<{col_widths[i]}}" for i in range(len(data[0])))
    print(header)
    print("-" * len(header))  # Garis pemisah

    # Mencetak baris tabel
    for row in data[1:]:
        print(" | ".join(f"{str(item):<{col_widths[i]}}" for i, item in enumerate(row)))


class Process:
    """Class untuk memproses dan memvalidasi data."""
    @staticmethod
    def validasi(data):
        try:
            if not data.nama.replace(" ", "").isalpha():
                raise ValueError("Nama harus hanya berisi huruf.")
            if not data.nim.isdigit():
                raise ValueError("NIM harus berupa angka.")
            if not data.nilai_uas.isdigit():
                raise ValueError("Nilai UAS harus berupa angka.")
            
            # Konversi nilai UAS ke int
            data.nilai_uas = int(data.nilai_uas)
            if data.nilai_uas < 0 or data.nilai_uas > 100:
                raise ValueError("Nilai UAS harus berada dalam rentang 0-100.")
            return True
        except ValueError as e:
            print(f"Error: {e}")
            return False


def main():
    data_list = []
    while True:
        print("\n=== Program Data Nilai UAS ===")
        print("\n1. Tambah Data\n2. Tampilkan Data\n3. Keluar")
        pilihan = input("Pilih menu: ").strip()
        if pilihan == "1":
            data = View.input_data()
            if Process.validasi(data):
                data_list.append(data)
                print("Data berhasil ditambahkan.")
        elif pilihan == "2":
            if data_list:
                View.tampilkan_data(data_list)
            else:
                print("Belum ada data.")
        elif pilihan == "3":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()
