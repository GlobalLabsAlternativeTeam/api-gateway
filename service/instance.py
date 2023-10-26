from abc import ABC, abstractmethod


class InstaceInterFace(ABC):
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
