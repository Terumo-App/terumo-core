from abc import ABC, abstractmethod


class Image(ABC):
    @property
    @abstractmethod
    def id(self) -> int:
        pass


class Picture:
    def __init__(self, large, medium, thumbnail):
        self.large = large
        self.medium = medium
        self.thumbnail = thumbnail


class Name:
    def __init__(self, last):
        self.last = last


class ImageEntity:
    def __init__(self, id: int, image_url: str, picture: Picture, name:Name):
        self.id = id
        self.image_url = image_url
        self.picture = picture
        self.name = name

