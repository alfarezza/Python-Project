import os
import pandas as pd
from tkinter import Tk, filedialog, messagebox

# Membuat jendela Tkinter
root = Tk()
root.withdraw()  # Menyembunyikan jendela utama

# Memilih folder input
folder_path = filedialog.askdirectory(title="Pilih Folder yang Berisi File PDF")

if folder_path:
    data = []

    # Membaca semua file PDF di folder
    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.pdf'):
            base_name = filename[:-4]
            if ' - ' in base_name:
                name, doc_no = base_name.split(' - ', 1)
                data.append({'Name': name.strip(), 'No Document': doc_no.strip()})
            else:
                data.append({'Name': base_name.strip(), 'No Document': ''})  # fallback

    # Buat DataFrame dari data
    df = pd.DataFrame(data)

    # Pilih lokasi dan nama file Excel output
    output_file = filedialog.asksaveasfilename(
        title="Simpan sebagai",
        defaultextension=".xlsx",
        filetypes=[("Excel files", "*.xlsx")]
    )

    if output_file:
        try:
            df.to_excel(output_file, index=False)
            messagebox.showinfo("Sukses", f"File berhasil disimpan di:\n{output_file}")
        except Exception as e:
            messagebox.showerror("Gagal Menyimpan", f"Terjadi kesalahan:\n{str(e)}")
    else:
        messagebox.showinfo("Dibatalkan", "Proses penyimpanan dibatalkan.")
else:
    messagebox.showinfo("Dibatalkan", "Folder tidak dipilih.")