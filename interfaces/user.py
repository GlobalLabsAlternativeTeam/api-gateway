from abc import ABC, abstractmethod


class UserInterFace(ABC):
    @abstractmethod
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def GetUsers(self, context):
        pass
