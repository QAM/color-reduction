from PIL import Image

from .template import Template


class NearestColor(Template):

    def run(self, image: Image) -> Image:
        return image
