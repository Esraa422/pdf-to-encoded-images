## PDF to Encoded Images Module

This project implements a module that converts PDF pages into images and encodes them.
It also supports different compression modes and allows controlling the maximum total size of the generated images.

## Features

- Convert PDF pages into images

- Encode images using JPEG or Base64

- Support compression modes: off, on, custom

- Control the maximum total size of the document images

## Project Structure

pdf_encoder/ → core module implementation
main.py → example script to run the module
examples/ → sample PDF files
tests/ → test files

## Requirements

Install the required libraries:

pip install -r requirements.txt

Note: This project uses pdf2image, which requires Poppler to be installed and available in the system PATH.

## How to Run

python main.py

## Example Usage

from pdf_encoder.processor import process_pdf

result = process_pdf("examples/Home_Task.pdf")