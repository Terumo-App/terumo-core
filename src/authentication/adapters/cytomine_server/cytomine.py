from typing import Union

from cytomine import Cytomine
from cytomine.models import Project, ProjectCollection, User, UserCollection

from authentication.domain.user.user_entity import UserEntity


class CytomineWrapper:
    def __init__(self, config) -> None:
        self._host = config.HOST
        self._public_key = config.PUBLIC_KEY
        self._private_key = config.PRIVATE_KEY
        self._global_project = config.GLOBAL_PROJECT

    def create_new_user(self, user: UserEntity) -> Union[float, bool]:
        with Cytomine(
            host=self._host,
            public_key=self._public_key,
            private_key=self._private_key,
        ):
            new_user = User(
                user.username,
                user.first_name,
                user.last_name,
                user.email,
                user.password,
            ).save()
            return new_user

    def get_user(self, username: str) -> Union[float, bool]:
        with Cytomine(
            host=self._host,
            public_key=self._public_key,
            private_key=self._private_key,
        ):
            users = UserCollection().fetch()
            user = [user for user in users.data() if user.username == username]
            if user:
                return user.pop()
            return False

    def add_user_global_project(self, user_id: int):
        with Cytomine(
            host=self._host,
            public_key=self._public_key,
            private_key=self._private_key,
        ):
            projects = ProjectCollection().fetch()
            proj_list = [
                proj
                for proj in projects.data()
                if proj.name == self._global_project
            ]
            if proj_list:
                global_project = proj_list.pop()
            else:
                # create global project if not exists
                global_project = Project(self._global_project).save()

            result = global_project.add_user(user_id)
            if result['status'] != 200:
                raise ValueError('Error adding user to the global project.')
