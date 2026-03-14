from pdf_encoder.image_encoder import image_to_jpeg_bytes



def get_image_size_bytes(image_bytes):
    return len(image_bytes)


def get_total_size_bytes(images_bytes):
    total_size = 0

    for image_bytes in images_bytes:
        total_size += len(image_bytes)

    return total_size


# Compress a single image using a given JPEG quality level
def compress_image(image, quality):
    jpeg_bytes = image_to_jpeg_bytes(image, quality)
    return jpeg_bytes

def compress_images(images, quality):
    compressed_images = []

    for image in images:
        jpeg_bytes = compress_image(image, quality)
        compressed_images.append(jpeg_bytes)

    return compressed_images


#compression_/logic
def apply_compression(images, compression_mode, max_total_size_bytes, quality=85):
    if compression_mode == "off":
        images_bytes = compress_images(images, quality)
        total_size = get_total_size_bytes(images_bytes)

        warning = None
        if total_size > max_total_size_bytes:
            warning = "Total image size exceeds the configured threshold."

        return images_bytes, total_size, warning

    elif compression_mode == "on":
        images_bytes = compress_images(images, quality)
        total_size = get_total_size_bytes(images_bytes)

        while total_size > max_total_size_bytes and quality > 10:
            quality -= 10
            images_bytes = compress_images(images, quality)
            total_size = get_total_size_bytes(images_bytes)

        return images_bytes, total_size, None

    elif compression_mode == "custom":
        images_bytes = compress_images(images, quality)
        total_size = get_total_size_bytes(images_bytes)

        if total_size <= max_total_size_bytes:
            return images_bytes, total_size, None

        while total_size > max_total_size_bytes and quality > 10:
            quality -= 10
            images_bytes = compress_images(images, quality)
            total_size = get_total_size_bytes(images_bytes)

        return images_bytes, total_size, None

    else:
        raise ValueError("Unsupported compression mode")
