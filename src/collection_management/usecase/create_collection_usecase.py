from collection_management.domain.collection.collection_repository_interface import (
    CollectionRepository,
)


class CreateColllectionUseCase:
    def __init__(self, collection_repository: CollectionRepository):
        self._collection_repository = collection_repository

    def execute(self, collection_name: str) -> int:

        existing_collection = (
            self._collection_repository.find_collection_by_name(
                collection_name
            )
        )
        if existing_collection:
            raise ValueError('Collection already exists')

        collection_data = self._collection_repository.create_collection(
            collection_name
        )
        return collection_data
