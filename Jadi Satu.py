# ==============================
# LATIHAN PYTHON DASAR
# ==============================

# 1. Deduplicasi
def deduplikasi(lst):
    hasil = []
    for item in lst:
        if item not in hasil:
            hasil.append(item)
    return hasil


# 2. Intersection
def intersection(arr1, arr2):
    hasil = []
    for x in arr1:
        if x in arr2 and x not in hasil:
            hasil.append(x)
    return hasil


# 3. Anagram
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)


# 4. First Recurring Character
def first_recurring_char(s):
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                return s[i]
    return None


# 5. Buku Telepon
def buku_telepon():
    kontak = {}

    while True:
        print("\n1. Tambah")
        print("2. Cari")
        print("3. Tampilkan")
        print("4. Keluar")

        pilih = input("Pilih: ")

        if pilih == "1":
            nama = input("Nama: ")
            nomor = input("Nomor: ")
            kontak[nama] = nomor

        elif pilih == "2":
            nama = input("Nama yang dicari: ")
            if nama in kontak:
                print("Nomor:", kontak[nama])
            else:
                print("Tidak ditemukan")

        elif pilih == "3":
            for nama in kontak:
                print(nama, ":", kontak[nama])

        elif pilih == "4":
            break


# ==============================
# MENU UTAMA
# ==============================

while True:
    print("\n=== MENU ===")
    print("1. Deduplicasi")
    print("2. Intersection")
    print("3. Anagram")
    print("4. First Recurring")
    print("5. Buku Telepon")
    print("6. Keluar")

    pilihan = input("Pilih: ")

    if pilihan == "1":
        data = list(map(int, input("Masukkan angka: ").split()))
        print("Hasil:", deduplikasi(data))

    elif pilihan == "2":
        a = list(map(int, input("List 1: ").split()))
        b = list(map(int, input("List 2: ").split()))
        print("Hasil:", intersection(a, b))

    elif pilihan == "3":
        s1 = input("String 1: ")
        s2 = input("String 2: ")
        print("Anagram?", is_anagram(s1, s2))

    elif pilihan == "4":
        s = input("Masukkan string: ")
        print("Hasil:", first_recurring_char(s))

    elif pilihan == "5":
        buku_telepon()

    elif pilihan == "6":
        break