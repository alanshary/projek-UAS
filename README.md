# Project-UAS

## Profil
| Variable | Isi |
| -------- | --- |
| **Nama** | Zaid Al Anshary |
| **NIM** | 312410315 |
| **Kelas** | TI.24.A.4 |
| **Mata Kuliah** | Bahasa Pemrograman |
| **Link vidio process** | https://youtube.com/shorts/RY74SR9VR-s?si=ZsVx4bLuXEOUNwea |


![gambar](https://github.com/Abcdeflahhh/UASPEMRO/blob/71de6bd92acac08a813c4d8179a0606b5037b7cd/Image/tugas.jpg)

- Class " Data " 
 
![uas data](https://github.com/user-attachments/assets/39fcce41-8111-4e0e-88f8-67bce48451b1)

Deskripsi: Class Data digunakan untuk menyimpan informasi tentang mahasiswa, termasuk nama, NIM (Nomor Induk Mahasiswa), dan nilai UAS.

Metode __init__: Ini adalah konstruktor yang dipanggil saat objek dari class Data dibuat. Ia menerima tiga parameter:

nama: Nama mahasiswa.

nim: Nomor Induk Mahasiswa.

nilai_uas: Nilai UAS yang diperoleh mahasiswa.

Atribut: Atribut self.nama, self.nim, dan self.nilai_uas menyimpan nilai yang diterima dari parameter.

- Class " View " 

![uas view](https://github.com/user-attachments/assets/12283e86-bebb-4c53-90ec-b2e6bf088759)

Deskripsi: Class View bertanggung jawab untuk interaksi dengan pengguna, termasuk pengambilan input dan menampilkan output.

Metode input_data:

Mengambil input dari pengguna untuk nama, NIM, dan nilai UAS.

Menggunakan strip() untuk menghapus spasi di awal dan akhir input.

Mengembalikan objek Data yang baru dibuat dengan informasi yang dimasukkan.

Metode tampilkan_data:

Menerima daftar objek Data (data_list) dan menyiapkan data untuk ditampilkan dalam format tabel.

Membuat header tabel dengan kolom "No", "Nama", "NIM", dan "Nilai UAS".

Menggunakan enumerate untuk menambahkan nomor urut pada setiap data.

Memanggil fungsi tampilkan_tabel untuk menampilkan data dalam format tabel.

- Fungsi " Tampilkan Table "

![uas](https://github.com/user-attachments/assets/fe1341f5-cc36-4179-b6d6-71b6d90467c0)

Deskripsi: Fungsi ini bertugas untuk menampilkan data dalam format tabel.

Proses:

Lebar Kolom: Menghitung lebar kolom berdasarkan panjang data terpanjang di setiap kolom menggunakan zip(*data) untuk mentransposisi data.

Header Tabel: Mencetak header tabel dengan format yang sesuai dan garis pemisah.

Baris Tabel: Mencetak setiap baris data dengan format yang sesuai, menggunakan enumerate untuk mendapatkan indeks dan item.

- Class " Process "

![uas process](https://github.com/user-attachments/assets/2acb1f56-ac26-4f71-8a83-0efb39c42d50)

Deskripsi: Metode ini adalah statis, yang berarti dapat dipanggil tanpa harus membuat instance dari class Process. Ia menerima satu parameter, yaitu objek Data.

Proses Validasi:

Nama: Memeriksa apakah nama hanya terdiri dari huruf. Jika tidak, akan mengangkat ValueError dengan pesan yang sesuai.

NIM: Memastikan bahwa NIM hanya berisi angka. Jika tidak, akan mengangkat ValueError.

Nilai UAS: Memeriksa apakah nilai UAS adalah angka. Jika tidak, akan mengangkat ValueError.

Konversi dan Rentang: Mengonversi nilai UAS dari string ke integer dan memeriksa apakah nilainya berada dalam rentang 0 hingga 100. Jika tidak, akan mengangkat ValueError.

Penanganan Kesalahan: Jika terjadi kesalahan selama validasi, pesan kesalahan akan dicetak, dan metode akan mengembalikan False. Jika semua validasi berhasil, metode akan mengembalikan 

True
