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
    def GetInstaceStatus(self, context, instance_id):
        pass

    @abstractmethod
    def GetTask(self, context, instance_id, task_id):
        pass

    @abstractmethod
    def IfTaskIsLocked(self, context, instance_id, task_id):
        pass

    @abstractmethod
    def GetTaskStatus(self, context, instance_id, task_id):
        pass

    @abstractmethod
    def CreateInstance(self, context, schema, patient_id, doctor_id):
        pass
