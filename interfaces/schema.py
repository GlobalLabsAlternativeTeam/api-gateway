from abc import ABC, abstractmethod


class SchemaInterface(ABC):
    @abstractmethod
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def GetSchema(self, context, schema_id):
        pass

    @abstractmethod
    def GetSchemas(self, context):
        pass

    @abstractmethod
    def CreateSchema(self, context, schema):
        pass

    @abstractmethod
    def UpdateSchema(self, context, schema):
        pass