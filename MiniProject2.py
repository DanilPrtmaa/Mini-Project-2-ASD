class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def tambah_di_awal(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def tambah_di_akhir(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def tambah_di_tengah(self, prev_node, data):
        if prev_node is None:
            print("Node sebelumnya tidak tersedia.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def hapus_di_awal(self):
        if self.head is None:
            print("Linked List kosong.")
            return
        temp = self.head
        self.head = self.head.next
        temp = None

    def hapus_di_akhir(self):
        if self.head is None:
            print("Linked List kosong.")
            return
        second_last = self.head
        while second_last.next.next:
            second_last = second_last.next
        second_last.next = None

    def hapus_di_tengah(self, prev_node):
        if prev_node is None or prev_node.next is None:
            print("Node sebelumnya tidak tersedia.")
            return
        temp = prev_node.next
        prev_node.next = temp.next
        temp = None

    def tampilkan(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


class Produk:
    def __init__(self, kode, nama, harga, stok, deskripsi):
        self.kode = kode
        self.nama = nama
        self.harga = harga
        self.stok = stok
        self.deskripsi = deskripsi

    def tampilkan_info(self):
        formatted_harga = "Rp {:,}".format(self.harga)
        print("Kode:", self.kode)
        print("Nama:", self.nama)
        print("Harga:", formatted_harga)
        print("Stok:", self.stok)
        print("Deskripsi:", self.deskripsi)
        print("------------------------")


class TokoElektronik:
    def __init__(self):
        self.produk_list = LinkedList()
        self.tambah_produk_otomatis()

    def tambah_produk_otomatis(self):
        produk1 = Produk("P001", "Laptop Asus Tuf Gaming F15", 10499000, 10, "Laptop gaming kelas atas dengan spesifikasi mumpuni.")
        self.tambah_produk(produk1)
        produk2 = Produk("P002", "Crystal UHD CU8000 4K Smart TV", 5799000, 15, "TV cerdas dengan resolusi 4K yang memukau.")
        self.tambah_produk(produk2)
        produk3 = Produk("P003", "LG Kulkas 2 Pintu GN-B195SQMT Smart Inverter", 3199000, 8, "Kulkas hemat energi dengan teknologi inverter.")
        self.tambah_produk(produk3)
        produk4 = Produk("P004", "Sanken Mesin Cuci Twin Turbo TW-882NP 9kg", 1599000, 12, "Mesin cuci dengan teknologi twin turbo yang cepat dan efisien.")
        self.tambah_produk(produk4)
        produk5 = Produk("P005", "AC Panasonic Premium Inverter CS-XU10VKP", 6900000, 7, "AC premium dengan teknologi inverter untuk hemat energi.")
        self.tambah_produk(produk5)

    def tambah_produk(self, produk):
        self.produk_list.tambah_di_akhir(produk)

    def lihat_produk(self):
        current = self.produk_list.head
        if current is None:
            print("Tidak ada produk dalam daftar.")
        else:
            print("Daftar Produk:")
            while current:
                current.data.tampilkan_info()
                current = current.next

    def update_produk(self, kode, **kwargs):
        current = self.produk_list.head
        while current:
            if current.data.kode == kode:
                for key, value in kwargs.items():
                    setattr(current.data, key, value)
                print("Produk dengan kode", kode, "telah diperbarui.")
                return
            current = current.next
        print("Produk dengan kode", kode, "tidak ditemukan.")

    def hapus_produk(self, kode):
        current = self.produk_list.head
        prev = None
        while current:
            if current.data.kode == kode:
                if prev is None:
                    self.produk_list.hapus_di_awal()
                else:
                    self.produk_list.hapus_di_tengah(prev)
                print("Produk dengan kode", kode, "telah dihapus.")
                return
            prev = current
            current = current.next
        print("Produk dengan kode", kode, "tidak ditemukan.")

    def tambah_menu(self):
        print("\nTambah Produk")
        kode = input("Masukkan kode produk: ")
        nama = input("Masukkan nama produk: ")
        harga = int(input("Masukkan harga produk: "))
        stok = int(input("Masukkan stok produk: "))
        deskripsi = input("Masukkan deskripsi produk: ")
        produk_baru = Produk(kode, nama, harga, stok, deskripsi)
        self.tambah_produk(produk_baru)

    def update_menu(self):
        print("\nUpdate Produk")
        kode = input("Masukkan kode produk yang ingin diupdate: ")
        print("Pilih atribut yang ingin diupdate:")
        print("1. Nama")
        print("2. Harga")
        print("3. Stok")
        print("4. Deskripsi")
        pilihan = int(input("Masukkan pilihan: "))
        if pilihan in [1, 2, 3, 4]:
            value = input("Masukkan nilai baru: ")
            if pilihan == 2 or pilihan == 3:
                value = int(value)
            self.update_produk(kode, **{["nama", "harga", "stok", "deskripsi"][pilihan - 1]: value})
        else:
            print("Pilihan tidak valid.")

    def hapus_menu(self):
        print("\nHapus Produk")
        kode = input("Masukkan kode produk yang ingin dihapus: ")
        self.hapus_produk(kode)

    def menu(self):
        while True:
            print("\nMenu:")
            print("1. Tambah Produk")
            print("2. Lihat Produk")
            print("3. Update Produk")
            print("4. Hapus Produk")
            print("5. Keluar")
            pilihan = int(input("Masukkan pilihan: "))
            if pilihan == 1:
                self.tambah_menu()
            elif pilihan == 2:
                self.lihat_produk()
            elif pilihan == 3:
                self.update_menu()
            elif pilihan == 4:
                self.hapus_menu()
            elif pilihan == 5:
                break
            else:
                print("Pilihan tidak valid.")


# Contoh penggunaan
if __name__ == "__main__":
    toko = TokoElektronik()
    toko.menu()
