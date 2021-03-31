from Program import *

def main():
    data = []
    def template():
        a = 1
        print("| No\t| Nama\t| Penawaran\t| Keuntungan Jual\t|")
        print("-------------------------------------------")
        for i in data:
            print("| {}\t| {}\t| {}\t| {}\t|".format(a, i.nama, i.jual, i.untung()))
            #
            a +=1
    
    print("======================================")
    data_pelelang = input("Nama Pemilik Tanah : ")
    panjang = int(input("Masukkan Panjang Tanah : "))
    luas = int(input("Masukkan lebar Tanah : "))
    harga_jual = int(input("Masukkan Harga Jual permeter : "))
    total_area = panjang * luas
    harga_total = harga_jual * total_area
    print("======================================")
    print("Nama pemilik = ",data_pelelang)
    print("Total tanah dijual ",total_area,"m^2")
    print("Harga total tanah ",harga_total)
    print("======================================")

    pelelang = int(input("Masukkan Jumlah pembeli = "))
    nomor = 1
    for i in range(pelelang):
        print("Pembeli ke-",nomor)
        nomor += 1
        nama = input("Masukkan nama penawar = ")
        jual = int(input("Masukkan jumlah tawaran = " ))
        while jual <= harga_total:
            jual = int(input("Kurang dari harga awal Masukan kembali jumlah tawaran "))
            if jual > harga_total:
                break

        data_baru = Program(nama, panjang, luas, jual, harga_jual, total_area, harga_total)
        data.append(data_baru)
        print("")

    template()

    def menu():
        pil = input("Apakah Data sudah benar ? (y/n)")
        if(pil=='n' or pil=="N"):
            option = int(input("""Apa yang ingin dirubah ?
            1. Nama Pembeli
            2. Jumlah yang ditawar
            3. Hapus penawar
            4. Tambah penawar
            5. exit
            """))
            if option == 1:
                pilU = int(input("Pelelang nomor "))
                dataBaru = str(input("Siapa namanya ?"))
                data[pilU-1].nama = dataBaru
                print("Data Sudah di Konfirmasi")
                template()
                menu()

            if option == 2:
                pilU = int(input("Pelelang nomor "))
                dataBaru = int(input("Berapa yanng ingin dibeli ?"))
                data[pilU-1].jual = dataBaru
                print("Data Sudah di Konfirmasi")
                template()
                menu()

            if option == 3:
                pilH = int(input("Pelelang nomor berapa ? "))
                del data[pilH-1]
                print("Data Sudah di Konfirmasi")
                template()
                menu()

            if option == 4:
                nomor = 1
                pelelang2 = int(input("Masukkan Jumlah pembeli = "))
                for i in range(pelelang2):
                    print("Pembeli ke-",nomor)
                    nomor += 1
                    nama = input("Masukkan nama penawar = ")
                    jual = int(input("Masukkan jumlah tawaran = " ))
                    data_baru = Program(nama, panjang, luas, jual, harga_jual, total_area, harga_total)
                    data.append(data_baru)
                    print("Data Sudah di Konfirmasi")
                    template()
                    menu()

            if option == 5:
                print("")
        else:
            print("Data Sudah di Konfirmasi")

    menu()
    template()

    #Analisa
    min = 100
    max = 0
    pMin = ''
    pMax = ''
    for i in data :
        if i.untung() < max:
            min = i.untung()
            pMin = i.nama
        if i.untung() > max:
            max = i.untung()
            pMax = i.nama

    print("============================================================================")
    
    print("Tanah terjual dengan harga tertinggi kepada {} , keuntungan pemilik {}".format(pMax, max))

    print("============================================================================")

if __name__ == "__main__":
    main()






