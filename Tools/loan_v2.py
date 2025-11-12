def amortization_schedule(rate_annual, nper, pv, payment_type):
    # Konversi bunga tahunan ke bulanan
    rate = rate_annual / 12 / 100

    # Hitung cicilan bulanan (annuitas)
    payment = (pv * rate) / (1 - (1 + rate) ** -nper)

    balance = pv
    schedule = []

    for period in range(1, nper + 1):
        interest = balance * rate
        principal = payment - interest

        # Khusus untuk pembayaran di awal bulan (type = 1)
        if payment_type == 1 and period == 1:
            # Belum ada bunga di awal bulan pertama
            interest = 0
            principal = payment
        elif payment_type == 1:
            # Periode selanjutnya: bunga dihitung dari sisa pinjaman sebelumnya
            interest = balance * rate
            principal = payment - interest

        balance -= principal
        balance = max(balance, 0)  # Hindari nilai negatif

        schedule.append({
            "Bulan": period,
            "Cicilan": round(payment, 2),
            "Bunga": round(interest, 3),
            "Pokok": round(principal, 3),
            "Sisa Pinjaman": round(balance, 3)
        })

    return schedule


# ==== User Input ====
print("=== Jadwal Cicilan Pinjaman (Amortisasi Schedule) ===")
rate = float(input("Masukkan bunga per tahun (%): "))
nper = int(input("Masukkan total periode (bulan): "))
pv = float(input("Masukkan jumlah pinjaman (Rp): "))
payment_type = int(input("Tipe pembayaran (0 = akhir bulan, 1 = awal bulan): "))

# Generate schedule
schedule = amortization_schedule(rate, nper, pv, payment_type)

# Tampilkan hasil
print("\nJadwal Cicilan Lengkap:\n")
print(f"{'Bulan':<6}{'Cicilan':>12}{'Bunga':>15}{'Pokok':>15}{'Sisa Pinjaman':>18}")
print("-" * 60)
for item in schedule:
    print(f"{item['Bulan']:<6}{item['Cicilan']:>12,.2f}{item['Bunga']:>15,.3f}{item['Pokok']:>15,.3f}{item['Sisa Pinjaman']:>18,.3f}")