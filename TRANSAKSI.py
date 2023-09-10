class Produk:
    def __init__(self, id_belanja, nama_barang, jumlah, harga, total_transaksi):
        self.id_belanja = id_belanja
        self.nama_barang = nama_barang
        self.jumlah = jumlah
        self.harga = harga
        self.total_transaksi = total_transaksi
    

    def display(self):
        print(f"{self.id_belanja :<4} | {self.nama_barang :<17} | {self.jumlah :<9} | {self.harga :<15} | {self.total_transaksi :<15}")

    

class Transaksi:

    def __init__(self):
        '''Fungsi untuk menginisialilasi list yang digunakan dalam program ini'''
    
        self.produk_list = []
        self.keranjang_list = []
        self.jumlah_list= []
        self.harga_list = []
        self.total_transaksi = []
        self.product_list = []


    def input_data(self):
        '''Fungsi untuk menambahkan data yang terdiri dari id_belanja, nama, jumlah barang, dan harga barang pada list.
        id_belanja (string), jumlah (int), harga (int), harga (int), total_transaksi (int)'''
        
        while True:
                
            id_belanja = (input("Masukkan ID: "))
            nama_barang = input("Masukkan Nama Barang: ")
            jumlah = int(input("Masukan Jumlah: "))
            harga = int(input("Masukan Harga: "))
               
            self.produk_list.append(nama_barang)
            self.jumlah_list.append(jumlah)
            self.harga_list.append(harga)
            total_transaksi = int(jumlah * harga)
            self.total_transaksi.append(total_transaksi)
            product_list = Produk(id_belanja, nama_barang, jumlah, harga, total_transaksi)
            self.product_list.append(product_list)

            print("Barang berhasil ditambah!!")

            self.tanya()
            break



    def delete_data(self, id_belanja):
        '''Fungsi untuk menghapus data yang terdiri dari id, nama, jumlah barang, dan harga barang pada list.
        id_belanja (string) = masukkan id belanja yang ingin dihapus'''

        for barang in self.product_list:
            if barang.id_belanja == id_belanja:
                self.product_list.remove(barang)
                print("Data berhasil dihapus!")
                return 
            
        else:
            print("Data tidak ditemukan!")
            


    def update_data(self, id_belanja):
        '''fungsi untuk mengubah data list belanja. Di fungsi ini bisa digunakan mengubah nama (string), jumlah (int),
        harga(int). Tinggal memasukkan nilai baru pada bagian yang tersedia.'''

        for barang in self.product_list:
            if barang.id_belanja == id_belanja:
                nama_barang = input("Masukkan Nama Barang Baru: ")
                jumlah = int(input("Masukan Jumlah Baru: "))
                harga = int(input("Masukkan Harga Baru: "))
                barang.nama_barang = nama_barang
                barang.jumlah = jumlah
                barang.harga = harga
                barang.total_transaksi = int(jumlah * harga)

                print("Data berhasil diubah!")

                return
        else:
            print("Data tidak ditemukan!")


    def display(self):
        print(f"{self.id_belanja :<4} | {self.nama_barang :<17} | {self.jumlah :<9} | {self.harga :<15} | {self.total_transaksi :<15}")

    def header(self):
        print("="*65)
        print(f"{'NO':<4} | {'Nama Barang':<17} | {'Jumlah':<9} | {'Harga':<15} | {'Total':<15}")
        print("="*65)


    def display_data(self):
        '''Fungsi display untuk menampilkan data yang sudah dimasukkan.'''

        for barang in self.product_list:
            barang.display()


    def reset_transaksi(self):
        '''Fungsi reset untuk menghapus semua isi dalam list. Fungsi ini akan berjalan ketika user
        membatalkan atau menyelesaikan transaksi'''

        self.product_list.clear()
       
    
    def reset_totalbayar(self):
        self.total_transaksi.clear()
   
    def total_bayar(self):
        '''Fungsi ini memproses pembayaran. total_bayar (int), diskon, total_belanja (int)'''

        total_bayar = sum(self.total_transaksi)
       
        if self.product_list:
            
            if total_bayar>=500_000:
                diskon = int(total_bayar*0.1)
                total_belanja = int(total_bayar-diskon)
                print(f"Total belanja Anda Rp {total_bayar}.\nAnda dapat diskon 10% sebesar Rp {diskon}.\nTotal belanja Rp {total_belanja} (sudah termasuk diskon)\n")
                try:
                    uang = int(input("Uang Pembayaran: "))
                except ValueError:
                    print("Masukkan nominal berupa angka!!")
                    uang = int(input("Uang Pembayaran: Rp "))
                
                if uang >= total_belanja:
                    print(f"Uang Kembalian: Rp {uang - total_belanja}")
                    self.reset_transaksi()
                    self.reset_totalbayar()
                    print("Terima kasih atas kunjungannya!")
                else:
                    print("UANG TIDAK CUKUP!!!\n")
                    self.batal()

            elif total_bayar>=300_000:
                diskon = int(total_bayar*0.08)
                total_belanja = int(total_bayar-diskon)
                print(f"Total belanja Anda Rp {total_bayar},\nAnda dapat diskon 8% sebesar Rp {diskon}.\nTotal belanja Rp {total_belanja} (sudah termasuk diskon)")

                try:
                    uang = int(input("Uang Pembayaran: "))
                except ValueError:
                    print("Masukkan nominal berupa angka!!")
                    uang = int(input("Uang Pembayaran: Rp "))

                if uang >= total_belanja:
                    print(f"Uang Kembalian: Rp {uang - total_belanja}")
                    self.reset_transaksi()
                    self.reset_totalbayar()
                    print("Terima kasih atas kunjungannya!")
                else:
                    print("UANG TIDAK CUKUP!!!\n")
                    self.batal()

            elif total_bayar>=200_000:
                diskon = int(total_bayar*0.05)
                total_belanja = int(total_bayar-diskon)
                print(f"Total belanja Anda Rp {total_bayar},\nAnda dapat diskon 5% sebesar Rp {diskon}.\nTotal belanja Rp {total_belanja} (sudah termasuk diskon)")
            
                try:
                    uang = int(input("Uang Pembayaran: "))
                except ValueError:
                    print("Masukkan nominal berupa angka!!")
                    uang = int(input("Uang Pembayaran: Rp "))

                if uang >= total_belanja:
                    print(f"Uang Kembalian: Rp {uang - total_belanja}")
                    self.reset_transaksi()
                    self.reset_totalbayar()
                    print("Terima kasih atas kunjungannya!")
                else:
                    print("UANG TIDAK CUKUP!!!\n")
                    self.batal()

            else:
                print(f"Total belanja Anda adalah Rp {total_bayar}.")
                
                try:
                    uang = int(input("Uang Pembayaran: "))
                except ValueError:
                    print("Masukkan nominal berupa angka!!")
                    uang = int(input("Uang Pembayaran: Rp "))

                if uang >= total_bayar:
                    print(f"Uang Kembalian: Rp {uang - total_bayar}")
                    self.reset_transaksi()
                    self.reset_totalbayar()
                    print("Terima kasih atas kunjungannya!")
                else:
                    print("UANG TIDAK CUKUP!!!\n")
                    self.batal()
        
        else:
            print("Total belanja belum bisa dihitung. Masih ada kesalahan input.")


    def tanya(self):
        print("--------------------")
        tanya = input("Ingin tambah barang? (y/t): ")
        print("--------------------")

        if tanya == "y":
            self.input_data()
        elif tanya == "t":
            self.header()
            self.display_data()
            
        else:
            print("Pilihan yang Anda masukkan salah!")


    def batal(self):
        '''Fungsi untuk melanjutkan proses pembayaran ketika user kekurangan uang.
        Fungsi ini akan mengarahkan untuk melanjutkan pembayaran atau pembatalan transaksi'''
        print("--------------------")
        tanya = input("Lanjut Pembayaran? (y/t): ")
        print("--------------------")

        if tanya == "y":
            self.total_bayar()
        elif tanya == "t":
            print("Anda membatalkan transaksi!!")
            main()
        else:
            print("Pilihan yang Anda masukkan salah!")
            
    

def main():
    '''Menu tampilan awal ketika program dijalankan.'''

    cashier = Transaksi()
    while True:
        print("\nMenu Kasir:")
        print("1. Input Barang Belanja")
        print("2. Hapus Barang Belanja")
        print("3. Ubah Daftar Belanja")
        print("4. Lihat Keranjang")
        print("5. Pembayaran")
        print("6. Keluar")

        pilihan = input("\nPilih Menu: ")

        if pilihan == "1":
            cashier.input_data()
        elif pilihan == "2":
            id = input("Masukkan ID yang ingin dihapus: ")
            cashier.delete_data(id)
        elif pilihan == "3":
            id = input("Masukkan ID yang ingin diubah: ")
            cashier.update_data(id)            
        elif pilihan == "4":
            cashier.header()
            cashier.display_data()
        elif pilihan == "5":
            cashier.total_bayar()
        elif pilihan == "6":
            cashier.reset_transaksi()
            print("Terima Kasih!")
            break
         
        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()

   