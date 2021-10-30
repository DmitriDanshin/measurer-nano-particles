import base64


def from_base64(image):
    with open('image.png', 'wb') as image_file:
        decoded_image_data = base64.decodebytes(image.img_base64)
        image_file.write(decoded_image_data)
