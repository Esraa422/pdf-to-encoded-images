import base64
import io


def image_to_jpeg_bytes(image, quality: int = 85):
    buffer = io.BytesIO()

    image = image.convert("RGB")
    image.save(buffer, format="JPEG", quality=quality)
    jpeg_bytes = buffer.getvalue()
    
    return jpeg_bytes


def encode_image(image, encoding_type: str = "base64", quality: int = 85):

    jpeg_bytes = image_to_jpeg_bytes(image, quality)

    if encoding_type == "jpeg":
        return jpeg_bytes

    elif encoding_type == "base64":
        encoded = base64.b64encode(jpeg_bytes)
        return encoded.decode("utf-8")

    else:
        raise ValueError("Unsupported encoding type")