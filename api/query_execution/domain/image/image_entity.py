from abc import ABC, abstractmethod


class ImageFileEntity:
    def __init__(self, binary: bytes, name: str):
        self.binary = binary
        self.name = name


class ImageEntity:
    def __init__(self, image_id: str, collection_id: int):
        self.image_id = image_id
        self.collection_id = collection_id


class ImageMetaDataEntity:
    def __init__(
        self,
        image_id: int,
        project: int,
        originalFilename: str,
        instanceFilename: str,
        path: str,
        thumb: str,
        preview: str,
        distance: float = None,
    ):
        self.image_id = image_id
        self.collection_id = project
        self.originalFilename = originalFilename
        self.instanceFilename = instanceFilename
        self.path = path
        self.thumb = thumb
        self.preview = preview
        self.distance = distance
