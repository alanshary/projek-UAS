# Project-UAS

## Profil
| Variable | Isi |
| -------- | --- |
| **Nama** | Zaid Al Anshary |
| **NIM** | 312410315 |
| **Kelas** | TI.24.A.4 |
| **Mata Kuliah** | Bahasa Pemrograman |
| **Link vidio Penjelasan** | ga usah liat liat |


![gambar](https://github.com/Abcdeflahhh/UASPEMRO/blob/71de6bd92acac08a813c4d8179a0606b5037b7cd/Image/tugas.jpg)

- Class " Data " 
 
![gambar](https://github.com/Abcdeflahhh/UASPEMRO/blob/b4c7185e51c5fabb70c80fe6a282a6c0386b8a15/Image/class%20data.jpg)

Deskripsi: Class Data digunakan untuk menyimpan informasi tentang mahasiswa, termasuk nama, NIM (Nomor Induk Mahasiswa), dan nilai UAS.

Metode __init__: Ini adalah konstruktor yang dipanggil saat objek dari class Data dibuat. Ia menerima tiga parameter:

nama: Nama mahasiswa.

nim: Nomor Induk Mahasiswa.

nilai_uas: Nilai UAS yang diperoleh mahasiswa.

Atribut: Atribut self.nama, self.nim, dan self.nilai_uas menyimpan nilai yang diterima dari parameter.

- Class " View " 

![gambar](https://github.com/Abcdeflahhh/UASPEMRO/blob/804b9c41bc554e0ff189d6b493c5b034950ff675/Image/class%20view.jpg)

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

![gambar](https://github.com/Abcdeflahhh/UASPEMRO/blob/cbac0eaedd66045259d5d8170e5f1de5c1f09817/Image/tampilkan%20table.jpg)

Deskripsi: Fungsi ini bertugas untuk menampilkan data dalam format tabel.

Proses:

Lebar Kolom: Menghitung lebar kolom berdasarkan panjang data terpanjang di setiap kolom menggunakan zip(*data) untuk mentransposisi data.

Header Tabel: Mencetak header tabel dengan format yang sesuai dan garis pemisah.

Baris Tabel: Mencetak setiap baris data dengan format yang sesuai, menggunakan enumerate untuk mendapatkan indeks dan item.

- Class " Process "

![gambar](https://github.com/Abcdeflahhh/UASPEMRO/blob/dcc49aba8a051f8459b3959fd85da8e8cfe64531/Image/class%20process.jpg)

Deskripsi: Metode ini adalah statis, yang berarti dapat dipanggil tanpa harus membuat instance dari class Process. Ia menerima satu parameter, yaitu objek Data.

Proses Validasi:

Nama: Memeriksa apakah nama hanya terdiri dari huruf. Jika tidak, akan mengangkat ValueError dengan pesan yang sesuai.

NIM: Memastikan bahwa NIM hanya berisi angka. Jika tidak, akan mengangkat ValueError.

Nilai UAS: Memeriksa apakah nilai UAS adalah angka. Jika tidak, akan mengangkat ValueError.

Konversi dan Rentang: Mengonversi nilai UAS dari string ke integer dan memeriksa apakah nilainya berada dalam rentang 0 hingga 100. Jika tidak, akan mengangkat ValueError.

Penanganan Kesalahan: Jika terjadi kesalahan selama validasi, pesan kesalahan akan dicetak, dan metode akan mengembalikan False. Jika semua validasi berhasil, metode akan mengembalikan 

True
