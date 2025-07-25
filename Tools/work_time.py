from datetime import datetime
from datetime import timedelta

# Waktu masuk dan keluar dalam format string
jam_masuk_str = "07:22:04"
jam_keluar_str = "16:10:59"

# Parsing string ke objek datetime
fmt = "%H:%M:%S"
jam_masuk = datetime.strptime(jam_masuk_str, fmt)
jam_keluar = datetime.strptime(jam_keluar_str, fmt)

# Hitung selisih waktu
durasi_hadir = jam_keluar - jam_masuk
# durasi_hadir -= timedelta(hours=1)

durasi_kerja = jam_keluar - jam_masuk
durasi_kerja -= timedelta(hours=0.5)

# Tampilkan durasi dalam jam, menit, dan detik
total_detik_hadir = durasi_hadir.total_seconds()
jam_hadir = int(total_detik_hadir // 3600)
menit_hadir = int((total_detik_hadir % 3600) // 60)
detik_hadir = int(total_detik_hadir % 60)

# Tampilkan durasi dalam jam, menit, dan detik
total_detik = durasi_kerja.total_seconds()
jam = int(total_detik // 3600)
menit = int((total_detik % 3600) // 60)
detik = int(total_detik % 60)


# print(f"Total waktu kehadiran: {jam_hadir} jam {menit_hadir} menit {detik_hadir} detik")
# print(f"Total waktu kerja: {jam} jam {menit} menit {detik} detik")
print(f"Total waktu kehadiran: {jam_hadir:02d}:{menit_hadir:02d}:{detik_hadir:02d}")
print(f"Total waktu kerja    : {jam:02d}:{menit:02d}:{detik:02d}")