from pdf_encoder.pdf_converter import convert_pdf_to_images
from pdf_encoder.image_encoder import encode_image


pdf_path = "examples/Home_Task.pdf"

images = convert_pdf_to_images(pdf_path)

print(f"Converted {len(images)} pages to images")

encoded_image = encode_image(images[0], encoding_type="base64", quality=85)


print(type(encoded_image))
print(encoded_image[:100])