class Barang:
    def __init__(self, id_barang, nama, harga, stok, kategori):
        self.id_barang = id_barang
        self.nama = nama
        self.harga = harga
        self.stok = stok
        self.kategori = kategori
        self.next = None

class TokoBangunan:
    def __init__(self):
        self.head = None

    def tambah_barang_di_awal(self, barang):
        barang.next = self.head
        self.head = barang

    def tambah_barang_di_akhir(self, barang):
        if not self.head:
            self.head = barang
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = barang

    def tambah_barang_di_antara(self, barang, id_sebelumnya):
        if not self.head:
            print("Linked list kosong.")
            return
        current = self.head
        while current:
            if current.id_barang == id_sebelumnya:
                barang.next = current.next
                current.next = barang
                return
            current = current.next
        print(f"Tidak ditemukan barang dengan ID {id_sebelumnya}. Barang tidak ditambahkan.")

    def hapus_barang_di_awal(self):
        if not self.head:
            print("Linked list kosong.")
            return
        self.head = self.head.next

    def hapus_barang_di_akhir(self):
        if not self.head:
            print("Linked list kosong.")
            return
        if not self.head.next:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def hapus_barang_di_antara(self, id_sebelumnya):
        if not self.head:
            print("Linked list kosong.")
            return
        if self.head.id_barang == id_sebelumnya:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.id_barang == id_sebelumnya:
                current.next = current.next.next
                return
            current = current.next
        print(f"Tidak ditemukan barang dengan ID {id_sebelumnya}. Barang tidak dihapus.")

    def tampilkan_barang(self):
        current = self.head
        while current:
            print(f"ID: {current.id_barang}, Nama: {current.nama}, Harga: {current.harga}, Stok: {current.stok}, Kategori: {current.kategori}")
            current = current.next

# Inisialisasi toko dan tambahkan barang
toko = TokoBangunan()
toko.tambah_barang_di_akhir(Barang(1, "Cat Tembok", 50000, 100, "Cat"))
toko.tambah_barang_di_akhir(Barang(2, "Paku", 1000, 200, "Perkakas"))
toko.tambah_barang_di_akhir(Barang(3, "Semenn", 75000, 50, "Material Bangunan"))
toko.tambah_barang_di_akhir(Barang(4, "Bor", 75000, 50, "Perkakas"))

# Tampilkan daftar barang
print("Daftar Barang:")
toko.tampilkan_barang()

# Contoh penggunaan CRUD
# tambah_barang_di_awal
toko.tambah_barang_di_awal(Barang(5, "Kuas", 20000, 150, "Cat"))
# hapus_barang_di_akhir
toko.hapus_barang_di_akhir()
# tambah_barang_di_antara
toko.tambah_barang_di_antara(Barang(6, "Cetakan Bata", 30000, 80, "Material Bangunan"), 2)
# hapus_barang_di_awal
toko.hapus_barang_di_awal()

# Tampilkan daftar barang setelah modifikasi
print("\nDaftar Barang setelah diubah:")
toko.tampilkan_barang()
