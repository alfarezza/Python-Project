import os
from pypdf import PdfReader, PdfWriter
from tkinter import Tk, filedialog

def merge_pdfs():
    # Matikan tampilan utama Tkinter
    root = Tk()
    root.withdraw()

    # Pilih file PDF yang akan digabung
    pdf_files = filedialog.askopenfilenames(
        title="Select PDF files to merge!",
        filetypes=[("PDF files", "*.pdf")]
    )

    if not pdf_files:
        print("No file is selected.")
        return

    # Pilih lokasi dan nama file output
    output_path = filedialog.asksaveasfilename(
        title="Save the merged file as",
        defaultextension=".pdf",
        filetypes=[("PDF files", "*.pdf")]
    )

    if not output_path:
        print("The storage location is not selected.")
        return

    # Proses penggabungan
    writer = PdfWriter()

    for pdf_file in pdf_files:
        reader = PdfReader(pdf_file)
        for page in reader.pages:
            writer.add_page(page)

    with open(output_path, "wb") as f_out:
        writer.write(f_out)

    print(f"The files were Merged Successfully and Saved as: {output_path}")

if __name__ == "__main__":
    merge_pdfs()
