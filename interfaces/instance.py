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

    @abstractmethod
    def GetPatients(self, context, doctor_id):
        pass

    @abstractmethod
    def CompleteTasks(self, instance_id, task_ids):
        pass

    @abstractmethod
    def CreateInstance(self, schema, patient_id, doctor_id):
        pass