def buku_telepon():
    kontak = {}
    
    while True:
        print("\n1. Tambah Kontak")
        print("2. Cari Kontak")
        print("3. Tampilkan Semua")
        print("4. Keluar")
        
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            nama = input("Masukkan nama: ")
            nomor = input("Masukkan nomor: ")
            kontak[nama] = nomor
            print("Kontak berhasil ditambahkan.")
            
        elif pilihan == "2":
            nama = input("Masukkan nama yang dicari: ")
            if nama in kontak:
                print("Nomor:", kontak[nama])
            else:
                print("Kontak tidak ditemukan.")
                
        elif pilihan == "3":
            for nama, nomor in kontak.items():
                print(f"{nama} : {nomor}")
                
        elif pilihan == "4":
            print("Keluar dari program.")
            break
            
        else:
            print("Pilihan tidak valid.")

# Jalankan program
buku_telepon()