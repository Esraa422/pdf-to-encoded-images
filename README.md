## PDF to Encoded Images Module

This project implements a module that converts PDF pages into images and encodes them.

It supports different compression modes and allows controlling the maximum total size of the generated images.

## Features

- Convert PDF pages into images

- Encode images using JPEG or Base64

- Support compression modes: off, on, custom

- Control the maximum total size of the document images

## Project Structure

pdf_encoder/ → core module implementation
main.py → example script to run the module
examples/ → sample PDF files
tests/ → basic tests

## Requirements

Install the required libraries:

pip install -r requirements.txt

Note: This project uses pdf2image, which requires Poppler to be installed and available in the system PATH.

## How to Run

python main.py

## Example Usage

from pdf_encoder.processor import process_pdf

result = process_pdf("examples/Home_Task.pdf")

## Example Input / Output

Input:
PDF file with multiple pages (e.g. 2–20 pages)

Output:

Processing PDF: examples/Home_Task.pdf  
Converted 2 pages to images  
Total size (MB): 0.42815589904785156  

{
  "warning": null
}

The warning field is returned when the total size exceeds the configured limit.

## Design Notes

The project is structured by separating responsibilities into different modules:

- PDF conversion

- compression logic

- encoding

- processing pipeline

A processor module is used to combine all steps into a single function for easier use.

## Additional Notes

Performance:
Processing time depends on the number of pages. The module performs efficiently for moderate-size PDFs.

Memory Usage:
All images are currently processed in memory. For very large PDFs, memory usage may increase.

Large PDFs:
The system supports multi-page documents. Future improvements could process pages sequentially to reduce memory usage.

Threshold Handling:
If the total image size exceeds the configured limit, a warning is returned.