from abc import ABC, abstractmethod


class Collection(ABC):
    @property
    @abstractmethod
    def id(self) -> int:
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        pass


class CollectionEntity(Collection):
    def __init__(
        self,
        id: int,
        created_at: str,
        name: str,
        num_of_images: int,
    ):
        self._id = id
        self._name = name
        self._created_at = created_at
        self._num_of_images = num_of_images

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name
