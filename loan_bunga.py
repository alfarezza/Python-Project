def cumipmt(rate_annual, nper, pv, start_period, end_period, payment_type):
    # Konversi suku bunga tahunan ke bulanan
    rate = rate_annual / 12 / 100

    # Hitung pembayaran bulanan (annuitas)
    payment = (pv * rate) / (1 - (1 + rate) ** -nper)

    total_interest = 0
    balance = pv

    for period in range(1, nper + 1):
        # Hitung bunga untuk periode ini
        interest = balance * rate

        # Hitung pokok yang dibayar di periode ini
        principal = payment - interest

        # Jika periode ada di antara start dan end, tambahkan ke total bunga
        if start_period <= period <= end_period:
            total_interest += interest

        # Kurangi sisa pinjaman
        balance -= principal

    return round(total_interest, 2)


# ==== User Input ====
print("=== Kalkulator CUMIPMT (Python) ===")
rate = float(input("Masukkan bunga per tahun (%): "))
nper = int(input("Masukkan total periode (bulan): "))
pv = float(input("Masukkan jumlah pinjaman (Rp): "))
start_period = int(input("Periode mulai (misal 1): "))
end_period = int(input("Periode akhir (misal 6): "))
payment_type = int(input("Tipe pembayaran (0 = akhir bulan, 1 = awal bulan): "))

# Jalankan fungsi
result = cumipmt(rate, nper, pv, start_period, end_period, payment_type)

# Output
print(f"\nTotal bunga yang dibayar dari bulan {start_period} sampai {end_period}: Rp {result:,.2f}")