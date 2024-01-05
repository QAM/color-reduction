from abc import ABC, abstractmethod
from PIL import Image


class Template(ABC):

    @abstractmethod
    def run(self, image: Image) -> Image:
        pass
