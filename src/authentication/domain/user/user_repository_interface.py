from abc import ABC, abstractmethod

from authentication.domain.user.user_entity import UserEntity


class UserRepository(ABC):
    @abstractmethod
    def create_user(self, user: UserEntity) -> int:
        pass

    @abstractmethod
    def find_user_by_username(self, username: str) -> bool:
        pass

    @abstractmethod
    def add_user_global_project(self, user_id: id) -> bool:
        pass
