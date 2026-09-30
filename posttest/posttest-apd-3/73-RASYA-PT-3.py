print("========================================")
print("     SISTEM TOP UP GAME OFFICIAL       ")
print("========================================")

username_input = input("Masukkan Username (Nama Panggilan) : ")
password_input = input("Masukkan Password (2 Digit NIM)    : ")

if username_input == "Rasya" and password_input == "73":
    print("\n[+] Login Berhasil! Selamat datang di Sistem Top Up.")
    print("----------------------------------------")
    
    id_player = input("Masukkan ID Player                  : ")
    
    # Pilih Game
    print("\nPilih Game:")
    print("1. Genshin Impact")
    print("2. Minecraft")
    print("3. Mobile Legends")
    pilihan_game = input("Pilih Game (1/2/3)                  : ")
    
    if pilihan_game == "1":
        nama_game = "Genshin Impact"
    elif pilihan_game == "2":
        nama_game = "Minecraft"
    elif pilihan_game == "3":
        nama_game = "Mobile Legends"
    else:
        nama_game = "Tidak Diketahui"


    print("\nPilih Kategori Top Up:")
    print("1. Kecil    (Rp 15.000)")
    print("2. Menengah (Rp 50.000)")
    print("3. Besar    (Rp 150.000)")
    pilihan_kategori = input("Pilih Kategori (1/2/3)              : ")
    
    if pilihan_kategori == "1":
        kategori = "Kecil"
        harga_dasar = 15000
    elif pilihan_kategori == "2":
        kategori = "Menengah"
        harga_dasar = 50000
    elif pilihan_kategori == "3":
        kategori = "Besar"
        harga_dasar = 150000
    else:
        kategori = "Tidak Valid"
        harga_dasar = 0

    # Pilih Metode Pembayaran
    print("\nPilih Metode Pembayaran:")
    print("1. Pulsa    (Admin Rp 2.500)")
    print("2. E-Wallet (Admin Rp 500)")
    pilihan_metode = input("Pilih Metode (1/2)                  : ")

    metode_bayar = "Pulsa" if pilihan_metode == "1" else "E-Wallet"


    biaya_admin = 2500 if pilihan_metode == "1" else 500

    total_bayar = harga_dasar + biaya_admin

    print("\n----------------------------------------")
    print(f"Total Pembayaran yang harus dibayar: Rp {total_bayar:,}")
    print("----------------------------------------")
    
    uang_dibayar = int(input("Masukkan nominal uang yang dibayarkan: Rp "))

    if uang_dibayar < total_bayar:
        print("\n[!] Transaksi Gagal Saldo tidak mencukupi")
    else:
        kembalian = uang_dibayar - total_bayar
        

        print("\n========================================")
        print("          STRUK PEMBELIAN TOP UP        ")
        print("========================================")
        print(f"ID Player         : {id_player}")
        print(f"Nama Game         : {nama_game}")
        print(f"Kategori Top Up   : {kategori}")
        print(f"Metode Pembayaran : {metode_bayar}")
        print(f"Biaya Admin       : Rp {biaya_admin:,}")
        print(f"Total Bayar       : Rp {total_bayar:,}")
        print(f"Uang Dibayar      : Rp {uang_dibayar:,}")
        print(f"Kembalian         : Rp {kembalian:,}")
        print("========================================")
        print("     Terima Kasih Telah Berbelanja!     ")
        print("========================================")

else:
    print("\n[!] Login Gagal. Username atau Password salah!")  