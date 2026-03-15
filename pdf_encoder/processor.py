import base64

from pdf_encoder.pdf_converter import convert_pdf_to_images
from pdf_encoder.compression import apply_compression


def process_pdf(
    pdf_path,
    compression_mode="custom",
    quality=85,
    max_total_size_mb=0.4,
    encoding_type="base64"
):
    #Convert PDF pages to PIL images
    images = convert_pdf_to_images(pdf_path)

    max_total_size_bytes = int(max_total_size_mb * 1024 * 1024)

    #Apply compression logic 
    images_bytes, total_size, warning = apply_compression(
        images=images,
        compression_mode=compression_mode,
        max_total_size_bytes=max_total_size_bytes,
        quality=quality
    )

    #Encode images
    encoded_images = []

    for img_bytes in images_bytes:
        if encoding_type == "jpeg":
            encoded_images.append(img_bytes)

        elif encoding_type == "base64":
            encoded = base64.b64encode(img_bytes).decode("utf-8")
            encoded_images.append(encoded)

        else:
            raise ValueError("Unsupported encoding type")

    return {
        "images": encoded_images,
        "total_size_bytes": total_size,
        "warning": warning,
        "page_count": len(images)
    }