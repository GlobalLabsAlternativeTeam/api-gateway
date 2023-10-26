from abc import ABC, abstractmethod


class UserInterFace(ABC):
    @abstractmethod
    def GetUsers(self, context):
        pass

    @abstractmethod
    def GetUser(self, context, user_id):
        pass