from view import View

def main():
    data_list = []
    while True:
        data = View.input_data()
        if data:
            data_list.append(data)
        else:
            print("Input data gagal. Silakan coba lagi.")
        
        # Tampilkan data
        View.tampilkan_data(data_list)
        
        # Tanya pengguna apakah ingin menambah data lagi
        lagi = input("Apakah Anda ingin menambah data lagi? (y/n): ").strip().lower()
        if lagi != 'y':
            break

if __name__ == "__main__":
    main()
