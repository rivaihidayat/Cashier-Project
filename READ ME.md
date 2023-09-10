##Python Project-Cashier Program
---
### A. Background
Seiring berkembangnya teknologi, penggunaan sebuah program komputer perlu diterapkan untuk memudahkan pekerjaan manusia. Salah satunya adalah program Cashier. Program ini bisa dimanfaatkan, khususnya pemilik toko dalam mengelola semua transaksi pembelian yang ada di toko miliknya. Pemilik sebagai user tidak perlu mencatat dan menghitung secara manual semua transaksi. Program Cashier ini akan menyelesaikan persoalan tersebut.


### B. Requirements
Dalam program kasir dibutuhkan beberapa fitur agar bisa memudahkan user dalam penggunaannya. Di program kasir ini dilengkapi dengan beberapa fitur, seperti:
1. menambahkan barang belanja
2. mengubah dan menghapus data transaksi (nama barang, jumlah, harga) pembelian jika terjadi kesalahan
3. menampilkan semua barang yang dibeli dalam transaksi. Termasuk rincian jumlah, harga, total pembelanjaan
4. melakukan pembayaran transaksi yang dilengkapi dengan perhitungan diskon apabila pembeli berbelanja dalam nominal tertentu.

Fitur-fitur diatas masih sangat sederhana, tetapi sudah bisa membantu untuk menunjang kebutuhan dasar dalam transaksi.

### C. Flowchart
Alur program dijelaskan menggunakan diagram alir atau flowchart. Ketika program dimulai, user akan langsung memasukkan id belanja, nama barang, jumlah barang, dan harga barang yang dibeli. Setelah selesai, user akan diajak untuk mengecek barang yang dibeli. Jika terjadi kesalahan pengisian nama, jumlah, dan harga barang, maka user bisa mengubah atau memilih untuk menghapusnya. Jika tidak ada kesalahan, maka user bisa melanjutkan ke proses pembayaran.

Dalam proses pembayaran terdapat kolom Total yang didapatkan dari hasil perhitungan jumlah * harga barang yang dibeli. Di proses pembayaran juga dilengkapi dengan perhitungan diskon apabila user berbelanja dalam nominal tertentu.

![Flowchart](https://masvay.com/wp-content/uploads/2023/09/Kasir.png)
### D. Test Case
Hasil beberapa fitur yang dicoba dalam program kasir ini.

##### 1. Add Item
Ketika proses menambahkan barang (Add Item) user hanya perlu memasukkan id belanja, nama barang(Str), jumlah(int), dan harga barang(int).

![Proses penambahan barang](https://masvay.com/wp-content/uploads/2023/09/proses-tambah.png)

Proses penambahan barang

![hasil tambah](https://masvay.com/wp-content/uploads/2023/09/hasil-penambahan.png)

Tampilan ketika barang sudah dimasukkan ke dalam keranjang.

##### 2. Update Item (Nama, Jumlah, dan Harga)
Fitur ubah nama barang, jumlah, dan harga (update item) dijadikan dalam satu proses. Jadi user akan memasukan semua perubahan dalam satu proses yang sama.

![proses ubah](https://masvay.com/wp-content/uploads/2023/09/proses-ubah.png)

Proses perubahan pada item belanja

##### 3. Delete Item
Fitur Delete item memungkinkan user untuk menghapus item. User tinggal memasukkan id belanja. Program akan membaca id tersebut dan kemudian menghapusnya.

![prose hapus](https://masvay.com/wp-content/uploads/2023/09/proses-hapus.png)

Proses Delete Item

![hasil hapus](https://masvay.com/wp-content/uploads/2023/09/hasil-hapus.png)

Tampilan setelah hapus salah satu item.

##### 4. Reset Transaction
Fitur reset transaction merupakan pengaturan untuk membuat semua list dalam keadaan kosong. Hal ini berguna karena transaksi sebelumnya tidak akan dieksekusi lagi.

![reset](https://masvay.com/wp-content/uploads/2023/09/reset-transaksi.png)

##### 5. Pemesanan Yang Sesuai
Sebelum proses bayar, user perlu memastikan barang yang dibeli sesuai dengan yang diharapkan. Termasuk jumlah dan harga yang sesuai dengan yang tertera.

![pesana](https://masvay.com/wp-content/uploads/2023/09/hasil-penambahan.png)

##### 6. Proses Pembayaran
Perhitungan pembayaran akan langsung menampilkan total transaksi user. Selain itu, program akan menampilkan besarnya diskon atau potongan jika user berbelanja dalam nominal tertentu. Informasi juga dilengkapi dengan harga setelah diskon dan besarnya uang kembalian.

![pembayaran](https://masvay.com/wp-content/uploads/2023/09/hasil-bayar.png)

### E. Kesimpulan
Program kasir ini masih sangat sederhana. Hanya menyediakan fitur-fitur dasar yang biasa dilakukan ketika berbelanja. Oleh sebab itu, program ini masih memungkinkan untuk terus dikembangkan sesuai dengan kebutuhan user. Beberapa fitur yang bisa dikembangakn antara lain adalah:
1. Penggunaan database untuk menampung setiap data traksaksi.
2. Penggunaan database memungkinkan untuk melihat alur kas (cash flow) secara periodik oleh pemilik toko.
3. Database dan cash flow bisa dimanfaatkan untuk mengatur strategi pemasaran yang cocok dalam pengembangan toko.
