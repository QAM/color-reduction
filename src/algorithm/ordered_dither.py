from PIL import Image

from .template import Template


class OrderedDither(Template):

    def run(self, image: Image) -> Image:
        return image
