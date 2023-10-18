from abc import ABC, abstractmethod


class CheckLoggedInInterface(ABC):
    @abstractmethod
    def execute(self, user_id: int) -> bool:
        pass
