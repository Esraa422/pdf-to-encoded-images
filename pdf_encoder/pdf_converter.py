from pathlib import Path
from pdf2image import convert_from_path



def convert_pdf_to_images(pdf_path: str):
    pdf_file = Path(pdf_path)

    if not pdf_file.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    images = convert_from_path(pdf_file)

    return images