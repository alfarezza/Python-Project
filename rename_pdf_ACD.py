import pdfplumber
import os
import re
import tkinter as tk
from tkinter import filedialog, messagebox

def extract_info_from_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        lines = []
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                lines += text.split('\n')

    nama = None
    nomor = None
    npwp = None

    # Cari semua Nama dan NPWP
    nama_matches = []
    npwp_matches = []

    # Loop untuk mencari semua Nama dan NPWP
    for line in lines:
        line = line.strip()

        # Mencari Nama setelah "NAMA :"
        nama_match = re.search(r'NAMA\s*:\s*(.*)', line, re.IGNORECASE)
        if nama_match:
            nama_matches.append(nama_match.group(1).strip())

        # Mencari NPWP
        npwp_match = re.search(r'NPWP\s*:\s*(\d+)', line)
        if npwp_match:
            npwp_matches.append(npwp_match.group(1).strip())

    # Ambil Nama dan NPWP dari bagian kedua
    if len(nama_matches) >= 2 and len(npwp_matches) >= 2:
        nama = nama_matches[2]  # Nama pada bagian kedua
        npwp = npwp_matches[1]  # NPWP pada bagian kedua

    # Cari nomor dokumen yang sesuai dengan pola MI-xxxxxxx
    for line in lines:
        line = line.strip()
        match = re.search(r'MI-\d+\.\d+', line)
        if match:
            nomor = match.group(0) 
            break


    return nama, npwp, nomor

def rename_pdf_in_directory(folder_path):
    total_processed = 0

    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.pdf'):
            total_processed += 1
            file_path = os.path.join(folder_path, filename)
            npwp, nama, nomor = extract_info_from_pdf(file_path)

            if nama and npwp and nomor:
                safe_nama = nama.replace('/', '-').replace('\\', '-')
                new_filename = f"{npwp} - {safe_nama}-{nomor}.pdf"
                new_path = os.path.join(folder_path, new_filename)

                try:
                    os.rename(file_path, new_path)
                    print(f"Renamed: {filename} → {new_filename}")
                except Exception as e:
                    print(f"Failed to rename {filename}: {e}")
            else:
                print(f"Incomplete data for: {filename}")

    return total_processed

# Ganti path di sini sesuai lokasi file PDF kamu

def main():
    root = tk.Tk()
    root.withdraw()  # Menyembunyikan jendela utama

    folder_path = filedialog.askdirectory(title="Select Folder Containing PDF Files")
    
    if not folder_path:
        messagebox.showinfo("Info", "No folder selected.")
        return

    total_files = rename_pdf_in_directory(folder_path)
    messagebox.showinfo(
        "Completed",
        f"Renaming process completed.\n"
        f"Total {total_files} PDF file(s) processed in:\n{folder_path}"
    )

if __name__ == "__main__":
    main()