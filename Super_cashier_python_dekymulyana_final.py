#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tabulate import tabulate

class Transaction:
    """
    Class untuk mengelola transaksi pembelian barang.
    """

    def __init__(self):
        """
        Inisialisasi objek transaksi dengan daftar pesanan kosong.
        """
        self.order_items = {}

    def add_item(self, nama_item, jumlah_item, harga_per_item):
        """
        Menambahkan item ke dalam daftar pesanan.

        Parameter:
            nama_item (str): Nama item.
            jumlah_item (int): Jumlah item berupa integer
            harga_per_item (int): Harga per item berupa integer.
        """
        try:
            jumlah_item = int(jumlah_item)
            harga_per_item = int(harga_per_item)
        except ValueError:
            raise ValueError("Jumlah item dan harga per item harus berupa angka.")

        item = {
            "Nama Item": nama_item,
            "Jumlah Item": jumlah_item,
            "Harga/Item": harga_per_item,
        }
        self.order_items[nama_item] = item

    def update_item_name(self, nama_item, update_nama_item):
        """
        Mengupdate nama item dalam daftar pesanan.

        Parameter:
            nama_item (str): Nama item yang akan diupdate.
            update_nama_item (str): Nama baru untuk item tersebut.
        """
        if nama_item in self.order_items:
            self.order_items[update_nama_item] = self.order_items.pop(nama_item)

    def update_item_qty(self, nama_item, update_jumlah_item):
        """
        Mengupdate jumlah item dalam daftar pesanan.

        Parameter:
            nama_item (str): Nama item yang akan diupdate jumlahnya.
            update_jumlah_item (int): Jumlah baru untuk item tersebut.
        """
        if nama_item in self.order_items:
            self.order_items[nama_item]["Jumlah Item"] = update_jumlah_item

    def update_item_price(self, nama_item, update_harga_item):
        """
        Mengupdate harga item dalam daftar pesanan.

        Parameter:
            nama_item (str): Nama item yang akan diupdate harganya.
            update_harga_item (int): Harga baru untuk item tersebut.
        """
        if nama_item in self.order_items:
            self.order_items[nama_item]["Harga/Item"] = update_harga_item

    def delete_item(self, nama_item):
        """
        Menghapus item dari daftar pesanan.

        Parameter:
            nama_item (str): Nama item yang akan dihapus.
        """
        if nama_item in self.order_items:
            del self.order_items[nama_item]

    def reset_transaction(self):
        """
        Mengosongkan daftar pesanan.
        """
        self.order_items = {}
        print("Daftar Pesanan Anda Berhasil Dikosongkan")

    def display_order(self):
        """
        Menampilkan daftar pesanan dalam bentuk tabel.
        """
        headers = ["No.", "Nama Item", "Jumlah Item", "Harga/Item", "Total Harga"]
        display_order = []

        for n, (nama_item, data_item) in enumerate(self.order_items.items(), start=1):
            item_qty, item_price = data_item["Jumlah Item"], data_item["Harga/Item"]
            total = item_qty * item_price
            display_order.append([n, nama_item, item_qty, item_price, total])

        print(tabulate(display_order, headers, tablefmt="fancy_grid"))

    def check_order(self):
        """
        Memeriksa validitas daftar pesanan.
        """
        error = any(
            not isinstance(nama_item, str) or not nama_item
            or not isinstance(item_data["Jumlah Item"], int) or not isinstance(item_data["Harga/Item"], int)
            or item_data["Jumlah Item"] <= 0 or item_data["Harga/Item"] <= 0
            for nama_item, item_data in self.order_items.items()
        )

        if error:
            raise ValueError("Terdapat kesalahan input data")
        else:
            print("Pemesanan sudah benar")
            print("\n")            
            print("Berikut Daftar Pemesanan Anda")
            self.display_order()

    def total_price(self):
        """
        Menghitung dan menampilkan total harga pesanan dengan atauran diskon.
        Jika total harga belanja lebih dari 500000 maka mendapatkan diskon sebesar 10%.
        Jika total harga belanja lebih dari 300000 maka mendapatkan diskon sebesar 8%.
        Jika total harga belanja lebih dari 200000 maka mendapatkan diskon sebesar 5%.
        Jika dibawah 200000 tidak mendapatkan diskon.
        """
        total_harga = sum(item["Jumlah Item"] * item["Harga/Item"] for item in self.order_items.values())
        discount = 0  # Default to no discount

        if total_harga > 500000:
            discount = 0.1  # 10% discount
        elif total_harga > 300000:
            discount = 0.08  # 8% discount
        elif total_harga > 200000:
            discount = 0.05  # 5% discount

        if discount > 0:
            discount_amount = total_harga * discount  # Calculate the discount amount
            total_harga -= discount_amount  # Apply the discount
            print(f"Total Belanja sebelum diskon: Rp {total_harga + discount_amount}")
            print(f"Anda Berhak Mendapatkan Diskon {discount * 100}%")
            print(f"Jumlah Diskon: Rp {discount_amount}")
            print(f"Yang harus dibayarkan setelah diskon: Rp. {total_harga}")
        else:
            print(f"Total Belanja: Rp {total_harga}")


# Contoh penggunaan:
trnset123 = Transaction()
trnset123.add_item("Mobil", 2, 100000)
trnset123.add_item("Mie", 1, 5000)
trnset123.add_item("Tempe", 3, 3000)

trnset123.update_item_name("Mobil", "Motor")
trnset123.update_item_qty("Mie", 2)
trnset123.update_item_price("Mie", 6000)
trnset123.delete_item("Tempe")

try:
    trnset123.check_order()
    trnset123.total_price()
except ValueError as e:
    print(f"Error: {e}")


