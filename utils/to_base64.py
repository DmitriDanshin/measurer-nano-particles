import base64


def to_base64(name="image.png"):
    with open(name, "rb") as image_file:
        image = base64.b64encode(image_file.read())
    return image
