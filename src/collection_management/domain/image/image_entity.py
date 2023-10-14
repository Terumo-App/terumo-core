from abc import ABC, abstractmethod


class Image(ABC):
    @property
    @abstractmethod
    def id(self) -> int:
        pass

    @property
    @abstractmethod
    def filename(self) -> str:
        pass


class ImageEntity(Image):
    def __init__(self, user_id: int, filename: str):
        self._id = user_id
        self._filename = filename

    @property
    def id(self) -> int:
        return self._id

    @property
    def filename(self) -> str:
        return self._filename
