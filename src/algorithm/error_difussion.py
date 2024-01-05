from PIL import Image

from .template import Template


class FloydSteinberg(Template):

    def run(self, image: Image) -> Image:
        return image


class Burkes(Template):

    def run(self, image: Image) -> Image:
        return image


class Stucki(Template):

    def run(self, image: Image) -> Image:
        return image
