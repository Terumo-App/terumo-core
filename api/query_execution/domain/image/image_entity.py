from abc import ABC, abstractmethod


class ImageFileEntity:
    def __init__(self, binary: bytes, name: str):
        self.binary = binary
        self.name = name


class ImageEntity:
    def __init__(self, image_id: str, collection_id: int):
        self.image_id = image_id
        self.collection_id = collection_id






class Picture:
    def __init__(self, large, medium, thumbnail):
        self.large = large
        self.medium = medium
        self.thumbnail = thumbnail


class Name:
    def __init__(self, last):
        self.last = last



class ImageMetaDataEntity:
    def __init__(self, 
                 id: int, 
                 image_url: str, 
                 picture: Picture, 
                 name: Name,
                 score: float=None
                 ):
        self.id = id
        self.image_url = image_url
        self.picture = picture
        self.name = name
        self.score = score
