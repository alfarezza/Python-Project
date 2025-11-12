def cumipmt_with_history(rate_annual, nper, pv, start_period, end_period, payment_type):
    # Konversi bunga tahunan ke bulanan
    rate = rate_annual / 12 / 100

    # Hitung pembayaran bulanan (annuitas)
    payment = (pv * rate) / (1 - (1 + rate) ** -nper)

    total_interest = 0
    balance = pv
    interest_history = {}

    for period in range(1, nper + 1):
        interest = balance * rate
        principal = payment - interest

        # Simpan history bunga jika periode dalam rentang
        if start_period <= period <= end_period:
            interest_history[period] = round(interest, 2)
            total_interest += interest

        # Update sisa pinjaman
        balance -= principal

    return round(total_interest, 2), interest_history


# ==== User Input ====
print("=== Kalkulator CUMIPMT dengan History (Python) ===")
rate = float(input("Masukkan bunga per tahun (%): "))
nper = int(input("Masukkan total periode (bulan): "))
pv = float(input("Masukkan jumlah pinjaman (Rp): "))
start_period = int(input("Periode mulai (misal 1): "))
end_period = int(input("Periode akhir (misal 6): "))
payment_type = int(input("Tipe pembayaran (0 = akhir bulan, 1 = awal bulan): "))

# Jalankan fungsi
total_interest, history = cumipmt_with_history(rate, nper, pv, start_period, end_period, payment_type)

# Output
print(f"\nTotal bunga yang dibayar dari bulan {start_period} sampai {end_period}: Rp {total_interest:,.2f}\n")
print("Rincian bunga per bulan:")
for month in range(start_period, end_period + 1):
    print(f"Bunga bulan ke-{month}: Rp {history[month]:,.2f}")