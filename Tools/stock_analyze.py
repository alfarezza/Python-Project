def hitung_investasi(jumlah_lot, harga_beli, harga_sekarang):
    LEMBAR_PER_LOT = 100
    jumlah_lembar = jumlah_lot * LEMBAR_PER_LOT

    # Nilai transaksi beli dan jual
    nilai_beli = jumlah_lembar * harga_beli
    nilai_jual = jumlah_lembar * harga_sekarang

    # === Biaya Beli ===
    fee_beli = 0.0019 * nilai_beli
    ppn_beli = 0.12 * fee_beli
    levy_beli = 0.0004 * nilai_beli
    total_biaya_beli = fee_beli + ppn_beli + levy_beli
    total_modal = nilai_beli + total_biaya_beli

    # === Biaya Jual ===
    fee_jual = 0.0029 * nilai_jual
    ppn_jual = 0.12 * fee_jual
    levy_jual = 0.0004 * nilai_jual
    pph_final = 0.001 * nilai_jual
    total_biaya_jual = fee_jual + ppn_jual + levy_jual + pph_final
    hasil_bersih_jual = nilai_jual - total_biaya_jual

    # === Gain/Loss ===
    gain_bersih = hasil_bersih_jual - total_modal
    persentase_gain = (gain_bersih / total_modal) * 100

    return {
        "jumlah_lembar": jumlah_lembar,
        "nilai_beli": nilai_beli,
        "total_modal": total_modal,
        "nilai_jual": nilai_jual,
        "hasil_bersih_jual": hasil_bersih_jual,
        "gain_bersih": gain_bersih,
        "persentase_gain": persentase_gain,
        "biaya_beli": total_biaya_beli,
        "biaya_jual": total_biaya_jual,
    }

# Input dari user
try:
    jumlah_lot = int(input("Masukkan jumlah lot yang dibeli: "))
    harga_beli = int(input("Masukkan harga beli per lembar: "))
    harga_sekarang = int(input("Masukkan harga saham saat ini per lembar: "))

    hasil = hitung_investasi(jumlah_lot, harga_beli, harga_sekarang)

    print("\n=== RINCIAN INVESTASI SAHAM ===")
    print(f"Jumlah lot              : {jumlah_lot}")
    print(f"Jumlah lembar           : {hasil['jumlah_lembar']}")
    print(f"Harga beli per lembar   : Rp {harga_beli:,}")
    print(f"Total nilai beli        : Rp {hasil['nilai_beli']:,.2f}")
    print(f"Total biaya beli        : Rp {hasil['biaya_beli']:,.2f}")
    print(f"Total modal             : Rp {hasil['total_modal']:,.2f} <--")
    print(f"Harga jual per lembar   : Rp {harga_sekarang:,.2f}")
    print(f"Total nilai jual        : Rp {hasil['nilai_jual']:,.2f}")
    print(f"Total biaya jual        : Rp {hasil['biaya_jual']:,.2f}")
    print(f"Nilai bersih penjualan  : Rp {hasil['hasil_bersih_jual']:,.2f} <--")
    print(f"Gain/Loss bersih        : Rp {hasil['gain_bersih']:,.2f}")
    print(f"Persentase gain/loss    : {hasil['persentase_gain']:.2f}%")

except ValueError:
    print("Input tidak valid. Harap masukkan angka saja.")