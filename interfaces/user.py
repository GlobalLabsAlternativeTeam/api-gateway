from abc import ABC, abstractmethod


class UserInterFace(ABC):
    @abstractmethod
    def GetUsers(self, context):
        pass