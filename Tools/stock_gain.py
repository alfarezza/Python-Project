def hitung_gain(jumlah_lot, harga_beli, harga_sekarang):
    LEMBAR_PER_LOT = 100
    jumlah_lembar = jumlah_lot * LEMBAR_PER_LOT
    gain_per_lembar = harga_sekarang - harga_beli
    total_gain = gain_per_lembar * jumlah_lembar
    return total_gain

# Ambil input dari pengguna
try:
    jumlah_lot = int(input("Masukkan jumlah lot yang dibeli: "))
    harga_beli = int(input("Masukkan harga beli per lembar (misal 180): "))
    harga_sekarang = int(input("Masukkan harga saham saat ini per lembar (misal 1551): "))

    # Hitung dan tampilkan hasil
    gain = hitung_gain(jumlah_lot, harga_beli, harga_sekarang)

    print("\n=== Hasil Perhitungan ===")
    print(f"Jumlah lot       : {jumlah_lot}")
    print(f"Jumlah lembar    : {jumlah_lot * 100}")
    print(f"Harga beli       : Rp{harga_beli:,}")
    print(f"Harga sekarang   : Rp{harga_sekarang:,}")
    print(f"Total gain       : Rp{gain:,}")

except ValueError:
    print("Input tidak valid. Pastikan kamu hanya memasukkan angka.")