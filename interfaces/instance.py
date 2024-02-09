from abc import ABC, abstractmethod


class InstaceInterface(ABC):
    @abstractmethod
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def GetInstances(self, context, patient_id):
        pass

    @abstractmethod
    def GetInstance(self, context, instance_id):
        pass
