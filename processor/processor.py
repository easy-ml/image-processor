import os

from PIL import Image


def process(image: Image, meta: dict, output: str, *args, **kwargs):
    """
    Change this function implementation
    :param image: PIL Image
    :param meta: Meta information
    :param output: Output folder
    :return: Dict with key as all output filenames and value as meta information about them
    """

    out_image = 'image.png'
    image.save(os.path.join(output, out_image))
    return {
        out_image: {
            'thumbnail': True
        }
    }
