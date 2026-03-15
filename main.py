from pdf_encoder.processor import process_pdf


pdf_path = "examples/Home_Task.pdf"

print("Processing PDF:", pdf_path)

result = process_pdf(pdf_path)

print(f"Converted {result['page_count']} pages to images")

print("Total size (MB):", result["total_size_bytes"] / (1024 * 1024))

if result["warning"]:
    print("Warning:", result["warning"])