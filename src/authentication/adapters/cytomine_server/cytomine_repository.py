from authentication.adapters.cytomine_server.cytomine import CytomineWrapper
from authentication.domain.user.user_entity import UserEntity
from authentication.domain.user.user_repository_interface import UserRepository


class CytomineRepository(UserRepository):
    cytomine: CytomineWrapper

    def __init__(self, config) -> None:
        self._cytomine = CytomineWrapper(config)

    def create_user(self, user: UserEntity):
        result = self._cytomine.create_new_user(user)
        if not result:
            raise ValueError('Error creating user.')
        return result

    def find_user_by_username(self, username: str):
        result = self._cytomine.get_user(username)
        return result

    def add_user_global_project(self, user_id: int):
        self._cytomine.add_user_global_project(user_id)
