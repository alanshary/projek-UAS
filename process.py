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
