from authentication.domain.user.user_entity import UserEntity
from authentication.domain.user.user_repository_interface import UserRepository


class SignupUseCase:
    def __init__(self, user_repository: UserRepository):
        self._user_repository = user_repository

    def execute(self, user: UserEntity) -> int:

        existing_user = self._user_repository.find_user_by_username(
            user.username
        )
        if existing_user:
            raise ValueError('User already exists')

        user_data = self._user_repository.create_user(user)
        self._user_repository.add_user_global_project(user_data.id)

        return user_data
