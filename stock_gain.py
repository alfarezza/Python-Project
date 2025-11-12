def hitung_gain(jumlah_lot, harga_beli, harga_sekarang):
    LEMBAR_PER_LOT = 100
    jumlah_lembar = jumlah_lot * LEMBAR_PER_LOT
    harga_beli_awal = jumlah_lembar * harga_beli
    gain_per_lembar = harga_sekarang - harga_beli
    total_gain = gain_per_lembar * jumlah_lembar
    total_aset = harga_sekarang * jumlah_lembar  # atau: harga_beli_awal + total_gain
    persentase_gain = (total_gain / harga_beli_awal) * 100
    return jumlah_lembar, harga_beli_awal, total_gain, total_aset, persentase_gain

# Ambil input dari pengguna
try:
    jumlah_lot = int(input("Masukkan jumlah lot yang dibeli: "))
    harga_beli = int(input("Masukkan harga beli per lembar (misal 180): "))
    harga_sekarang = int(input("Masukkan harga saham saat ini per lembar (misal 1551): "))

    # Hitung dan tampilkan hasil
    jumlah_lembar, harga_beli_awal, gain, total_aset, persentase_gain = hitung_gain(jumlah_lot, harga_beli, harga_sekarang)

    print("\n=== Hasil Perhitungan ===")
    print(f"Jumlah lot         : {jumlah_lot}")
    print(f"Jumlah lembar      : {jumlah_lembar}")
    print(f"Harga beli         : Rp {harga_beli:,}")
    print(f"Total harga beli   : Rp {harga_beli_awal:,}")
    print(f"Harga sekarang     : Rp {harga_sekarang:,}")
    print(f"Total gain         : Rp {gain:,}")
    print(f"Total nilai aset   : Rp {total_aset:,}")
    print(f"G/L Percentage     : {persentase_gain:.2f} %")

except ValueError:
    print("Input tidak valid. Pastikan kamu hanya memasukkan angka.")