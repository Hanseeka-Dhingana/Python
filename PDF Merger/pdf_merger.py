import PyPDF2
import os

def merge_pdfs_from_folder(folder_path, output_filename):
    merger = PyPDF2.PdfMerger()

    try:
        # Get all PDF files from the folder
        pdf_files = [
            file for file in os.listdir(folder_path)
            if file.lower().endswith(".pdf")
        ]

        if not pdf_files:
            print(f"File Not Found In {folder_path}.")
            return

        # (Optional) Sort files alphabetically
        pdf_files.sort()

        for pdf in pdf_files:
            pdf_path = os.path.join(folder_path, pdf)
            print(f"Adding {pdf}...")
            merger.append(pdf_path)

        merger.write(output_filename)
        merger.close()

        print(f"Success! All files merged into {output_filename}")

    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    folder_path = "./Data"   # Enter your folder name here
    output_file = "merged_document.pdf"

    merge_pdfs_from_folder(folder_path, output_file)
