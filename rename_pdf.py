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

    # Cari baris yang mengandung "NAMA :"
    for line in lines:
        if re.search(r'\bNAMA\b\s*:', line.upper()):
            nama_match = re.search(r'NAMA\s*:\s*(.*)', line, re.IGNORECASE)
            if nama_match:
                nama = nama_match.group(1).strip()
                break

    # Cari nomor dokumen yang sesuai dengan pola
    for line in lines:
        line = line.strip()
        match = re.search(r'\b(25[A-Za-z0-9]{7,})\b', line)
        if match:
            nomor = match.group(1)
            break

    return nama, nomor

def rename_pdf_in_directory(folder_path):
    total_processed = 0

    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.pdf'):
            total_processed += 1
            file_path = os.path.join(folder_path, filename)
            nama, nomor = extract_info_from_pdf(file_path)

            if nama and nomor:
                safe_nama = nama.replace('/', '-').replace('\\', '-')
                new_filename = f"{safe_nama} - {nomor}.pdf"
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
# folder_path = r'C:\Downloads\Teams\PDF'
# rename_pdf_in_directory(folder_path)

def main():
    root = tk.Tk()
    root.withdraw()  # Menyembunyikan jendela utama

    folder_path = filedialog.askdirectory(title="Select Folder Containing PDF Files")
    
    if not folder_path:
        messagebox.showinfo("Info", "No folder selected.")
        return

    # rename_pdf_in_directory(folder_path)
    # messagebox.showinfo("Selesai", f"Proses rename PDF di folder:\n{folder_path}\nselesai.")

    total_files = rename_pdf_in_directory(folder_path)
    messagebox.showinfo(
        "Completed",
        f"Renaming process completed.\n"
        f"Total {total_files} PDF file(s) processed in:\n{folder_path}"
    )

if __name__ == "__main__":
    main()