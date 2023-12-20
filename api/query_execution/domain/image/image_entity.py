from abc import ABC, abstractmethod
from typing import Dict, List


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
                 score: float=None,
                 vector: List[Dict[str, float]]=None,
                 query_vector: List[Dict[str, float]]=None,
                 ):
        self.id = id
        self.image_url = image_url
        self.picture = picture
        self.name = name
        self.score = score
        self.vector = vector
        self.query_vector = query_vector

    def set_vector(self, vector: List[float], attributes:List[str]):
        self.vector = []
        for att, att_name in zip(vector, attributes):
            self.vector.append({ 
                "attribute_name": att_name,
                "probability": att,
            })
            
    def set_query_vector(self, vector: List[float], attributes:List[str]):
        self.query_vector = []
        for att, att_name in zip(vector, attributes):
            self.query_vector.append({ 
                "attribute_name": att_name,
                "probability": att,
            })

