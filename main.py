from pdf_encoder.pdf_converter import convert_pdf_to_images
from pdf_encoder.image_encoder import encode_image
from pdf_encoder.compression import get_total_size_bytes
from pdf_encoder.compression import compress_images, get_total_size_bytes
from pdf_encoder.compression import apply_compression


pdf_path = "examples/Home_Task.pdf"

images = convert_pdf_to_images(pdf_path)

print(f"Converted {len(images)} pages to images")


# You can change the compression mode, quality, and max file size here
compression_mode = "custom"
quality=85
max_total_size_mb = 0.4
max_total_size_bytes = int(max_total_size_mb * 1024 * 1024)

images_bytes, total_size, warning = apply_compression(
    images=images,
    compression_mode=compression_mode,
    max_total_size_bytes=max_total_size_bytes,
    quality=quality
)


print("Max size (MB):", max_total_size_mb)
print("Compression mode:", compression_mode)
print("Total size (MB):", total_size / (1024 * 1024))

if warning:
    print("Warning:", warning)
