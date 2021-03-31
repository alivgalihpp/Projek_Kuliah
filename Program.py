class Program:
    def __init__(self, nama, panjang, luas, jual=0, harga_jual=0, total_area=0, harga_total=0):
        self.nama = nama
        self.panjang = panjang
        self.luas = luas
        self.jual = jual
        self.harga_jual = harga_jual
        self.total_area = total_area
        self.harga_total = harga_total

    def untung(self):
        b = self.jual - self.harga_total
        return b