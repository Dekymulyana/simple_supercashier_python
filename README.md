# simple_supercashier_python
Python Project Super Cashier - Deky Mulyana
# Super Cashier

## Deky Mulyana - Python Project Pacmann
#### Project ini merupakan aplikasi self-service sederhana di supermarket dengan menggunakan bahasa pemrograman Python 


## 0. Background
#### Andi adalah seorang pemilik supermarket besar di salah satu kota di Indonesia. Andi memiliki rencana untuk melakukan perbaikan proses bisnis, yaitu Andi akan membuat sistem kasir yang self-service di supermarket miliknya. Sehingga customer bisa langsung memasukkan item yang dibeli, jumlah item yang dibeli, dan harga item yang dibeli dan fitur yang lain. Sehingga customer yang tidak berada di kota tersebut bisa membeli barang dari supermarket tersebut. Setelah Andi melakukan riset, ternyata Andi memiliki masalah, yaitu Andi membutuhkan Programmer untuk membuatkan fitur-fitur agar bisa sistem kasir self-service di supermarket itu bisa berjalan dengan lancar.

## 1. Requirement/ Kebutuhan
#### Inisialisasi Transaksi
Kode dapat membuat objek transaksi dan daftar pesanan awalnya kosong.

#### Menambahkan Item
Kode dapat memungkinkan pengguna untuk menambahkan item ke daftar pesanan dengan nama, jumlah, dan harga per item.

#### Mengupdate Item
Kode dapat memungkinkan pengguna untuk mengubah nama, jumlah, atau harga per item dari item yang ada dalam daftar pesanan.

#### Menghapus Item
Kode dapat memungkinkan pengguna untuk menghapus item dari daftar pesanan berdasarkan nama itemnya.

#### Reset Transaksi
Kode dapat memungkinkan pengguna untuk mengosongkan daftar pesanan.

#### Menampilkan Daftar Pesanan
Kode dapat menampilkan daftar pesanan dalam bentuk tabel dengan nomor item, nama item, jumlah item, harga per item, dan total harga.

#### Memeriksa Validitas Daftar Pesanan
Kode dapat memeriksa apakah data dalam daftar pesanan valid, yaitu tipe data yang benar dan nilai yang valid.

#### Menghitung Total Harga
Kode dapat menghitung total harga pesanan dengan menerapkan diskon sesuai aturan yang telah ditentukan.


## 2. Flowchart
![Diagram SuperCashier](https://github.com/Dekymulyana/simple_supercashier_python/assets/16453391/a7fe86b2-09b0-4efd-802d-472d78577cd6)

## 3. Penjelasan Program
 ### a. __init__()
 Inisialisasi objek transaksi dengan daftar pesanan kosong.
 
 <img width="483" alt="image" src="https://github.com/Dekymulyana/simple_supercashier_python/assets/16453391/3e4a39ff-bbfb-4d34-bd2c-ef7057e2ec64">
 
 ### b. add_item
 Menambahkan item ke dalam daftar pesanan.

 Parameter:
 nama_item (str): Nama item.
 jumlah_item (int): Jumlah item berupa integer
 harga_per_item (int): Harga per item berupa integer.
     
 <img width="483" alt="image" src="https://github.com/Dekymulyana/simple_supercashier_python/assets/16453391/cfc5d9d8-9597-4d1d-9fba-2f40abc06fcd">

 ### c. update_item
 Mengupdate nama item dalam daftar pesanan.

 Parameter:
 nama_item (str): Nama item yang akan diupdate harganya.
 update_nama_item (str): Nama baru untuk item tersebut.
 update_jumlah_item (int): Jumlah baru untuk item tersebut.
 update_harga_item (int): Harga baru untuk item tersebut.
      
<img width="483" alt="image" src="https://github.com/Dekymulyana/simple_supercashier_python/assets/16453391/f5e88b7d-23e6-4e1b-95c0-b2c91c4f951a">

 ### d. delete_item
 Menghapus item dari daftar pesanan.

 Parameter:
 nama_item (str): Nama item yang akan dihapus.
 
<img width="483" alt="image" src="https://github.com/Dekymulyana/simple_supercashier_python/assets/16453391/ad43f24d-d0d1-4562-8906-10161b705415">

 ### e. reset_transaction
 Mengosongkan daftar pesanan.
 
<img width="483" alt="image" src="https://github.com/Dekymulyana/simple_supercashier_python/assets/16453391/e23824a8-4500-48e3-8af3-382ab70d8bb7">

 ### f. display_order
 Menampilkan daftar pesanan dalam bentuk tabel.
 
 <img width="483" alt="image" src="https://github.com/Dekymulyana/simple_supercashier_python/assets/16453391/7e680d17-278e-46d0-a5e9-99057fcdef4c">
 
 ### g. check_order
 Memeriksa validitas daftar pesanan.
 
 <img width="483" alt="image" src="https://github.com/Dekymulyana/simple_supercashier_python/assets/16453391/4164cc58-9139-4484-9b64-ffd98261947d">

 ### h. total_price
 Menghitung dan menampilkan total harga pesanan dengan atauran diskon.
 Jika total harga belanja lebih dari 500000 maka mendapatkan diskon sebesar 10%.
 Jika total harga belanja lebih dari 300000 maka mendapatkan diskon sebesar 8%.
 Jika total harga belanja lebih dari 200000 maka mendapatkan diskon sebesar 5%.
 Jika dibawah 200000 tidak mendapatkan diskon.
 
<img width="483" alt="image" src="https://github.com/Dekymulyana/simple_supercashier_python/assets/16453391/f618eb27-5d74-49f5-a370-5ed8d74ad8bc">


## 4. Uji Coba
 ### a. Test Case 1
<img width="483" alt="image" src="https://github.com/Dekymulyana/simple_supercashier_python/assets/16453391/0271c73c-084c-4959-a5d6-0e9c51244d06">

 ### b. Test Case 2
<img width="483" alt="image" src="https://github.com/Dekymulyana/simple_supercashier_python/assets/16453391/f4f58379-b1a7-4c21-ad20-98ddfafb2d25">


 ### c. Test Case 3
<img width="483" alt="image" src="https://github.com/Dekymulyana/simple_supercashier_python/assets/16453391/45e002af-04b3-460d-8c6b-6e810f1b3935">

 ### d. Test Case 4
<img width="483" alt="image" src="https://github.com/Dekymulyana/simple_supercashier_python/assets/16453391/a1467134-62c5-4c5c-bde4-985a55daaeb4">

## 5. Rekomendasi
 ### Buat dalam bentuk GUI agar lebih ramah pengguna, da antarmuka yang lebih interaktif.
 ### Tambahkan database untuk menyimpan data transaksi secara persisten.
 ### Buat Laporan Transaksi Tambahkan fitur untuk menghasilkan laporan transaksi, sehingga pengguna dapat melacak transaksi mereka dari waktu ke waktu.
