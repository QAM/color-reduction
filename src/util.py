import io
import os.path
from pathlib import Path

from PIL import Image


def read_image(image_path: str) -> Image:
    image_bytes = io.BytesIO(Path(image_path).read_bytes())
    image = Image.open(image_bytes)
    return image


def read_convert_to_8_bit_bmp(bmp_path):
    bmp_file = read_image(bmp_path)
    # https://stackoverflow.com/questions/49757471/how-to-convert-numpy-array-into-tuple/49757668
    # Based on the PIL spec https://pillow.readthedocs.io/en/stable/handbook/concepts.html
    # We only support RGB and P.
    if bmp_file.mode not in ('RGB', 'P', 'RGBA'):
        raise ValueError(f"artwork bmp format is {bmp_file.mode} but we only allow RGB or P")
    if bmp_file.mode != 'P':
        bmp_file = bmp_file.convert(
            "P", palette=Image.ADAPTIVE, colors=256)
    return bmp_file


def write_file(img: Image, output_folder: str, filename: str) -> None:
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    img.save(os.path.join(output_folder, filename))
