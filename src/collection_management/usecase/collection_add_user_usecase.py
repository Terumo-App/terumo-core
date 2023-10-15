from collection_management.domain.collection.collection_repository_interface import (
    CollectionRepository,
)


class AddUserUseCase:
    def __init__(self, collection_repository: CollectionRepository):
        self._collection_repository = collection_repository

    def execute(self, user) -> int:
        pass
