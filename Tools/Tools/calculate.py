def hitung_hpp():
    # Input variabel dari user
    bahan_per_baju = float(input("Kebutuhan bahan per baju (yard): "))
    harga_bahan_per_yard = float(input("Harga bahan per yard: "))
    harga_resleting = float(input("Harga resleting per pcs (jika ada, 0 jika tidak): "))
    furing_per_baju = float(input("Kebutuhan furing per baju (yard, jika tidak gunakan 0): "))
    harga_furing_per_yard = float(input("Harga furing per yard (jika tidak gunakan 0): "))

    jasa_potong_bahan = float(input("Jasa potong bahan per pcs: "))
    jasa_jahit = float(input("Jasa jahit per pcs: "))
    jasa_potong_furing = float(input("Jasa potong furing per pcs (jika tidak gunakan 0): "))

    # Biaya tetap per pcs (diubah menjadi biaya tetap)
    jasa_kancing = 1500 #include pasang dan lubang
    jasa_finishing_benang = 1000
    jasa_steam_baju = 1000
    packaging_charge = 500

    # Biaya tetap per pcs lainnya
    benang = 500
    kancing = 500
    ongkos_kirim = 2000
    biaya_overhead_listrik = 1000

    # Menghitung total biaya bahan
    total_bahan = (bahan_per_baju * harga_bahan_per_yard) + (furing_per_baju * harga_furing_per_yard) + harga_resleting

    # Menghitung total biaya jasa
    total_jasa = (jasa_potong_bahan + jasa_jahit + jasa_potong_furing)

    # Menghitung total biaya tetap dan overhead
    total_biaya_tetap = benang + kancing + ongkos_kirim + biaya_overhead_listrik + jasa_kancing + jasa_finishing_benang + jasa_steam_baju + packaging_charge

    # Menghitung HPP
    hpp = total_bahan + total_jasa + total_biaya_tetap

    # Input profit margin
    while True:
        profit_margin = float(input("Masukkan persentase profit margin (maks 50%): "))
        if profit_margin > 50:
            print("Peringatan: Profit margin tidak bisa lebih dari 50%. Mohon masukkan ulang.")
        else:
            break

    # Menghitung harga jual
    harga_jual = hpp * (1 + profit_margin / 100)

    print("\n--- Hasil Kalkulasi ---")
    print(f"Harga Pokok Produksi (HPP): {hpp}")
    print(f"Harga Jual (dengan {profit_margin}% profit): {harga_jual}")

# Jalankan fungsi
hitung_hpp()