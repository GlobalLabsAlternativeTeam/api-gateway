from google.protobuf.timestamp_pb2 import Timestamp
from models.types.task import Task

class Schema:
    def __init__(self, schema_id, author_id, schema_name, created_at, updated_at, deleted_at, patient, treatment_doctor, tasks):
        self.schema_id = schema_id
        self.author_id = author_id
        self.schema_name = schema_name
        self.created_at = created_at
        self.updated_at = updated_at
        self.deleted_at = deleted_at
        self.patient = patient
        self.treatment_doctor = treatment_doctor
        self.tasks = tasks

    @classmethod
    def from_proto(cls, proto_data):
        created_at = cls._timestamp_from_proto(proto_data.created_at)
        updated_at = cls._timestamp_from_proto(proto_data.updated_at)
        deleted_at = cls._timestamp_from_proto(proto_data.deleted_at)
        tasks = [Task.from_proto(task_proto) for task_proto in proto_data.tasks]
        return cls(
            proto_data.schema_id,
            proto_data.author_id,
            proto_data.schema_name,
            created_at,
            updated_at,
            deleted_at,
            proto_data.patient if proto_data.HasField("patient") else None,
            proto_data.treatment_doctor if proto_data.HasField("treatment_doctor") else None,
            tasks
        )

    def to_json(self):
        return {
            "schema_id": self.schema_id,
            "author_id": self.author_id,
            "schema_name": self.schema_name,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "deleted_at": self.deleted_at,
            "patient": self.patient,
            "treatment_doctor": self.treatment_doctor,
            "tasks": [task.to_json() for task in self.tasks]
        }

    @classmethod
    def from_json(cls, json_data):
        tasks = [Task.from_json(task_data) for task_data in json_data["tasks"]]
        return cls(
            json_data["schema_id"],
            json_data["author_id"],
            json_data["schema_name"],
            json_data["created_at"],
            json_data["updated_at"],
            json_data["deleted_at"],
            json_data["patient"],
            json_data["treatment_doctor"],
            tasks
        )

    def to_dict(self):
        return self.to_json()

    @classmethod
    def from_dict(cls, dict_data):
        return cls.from_json(dict_data)

    @staticmethod
    def _timestamp_to_proto(timestamp):
        timestamp_proto = Timestamp()
        timestamp_proto.seconds = timestamp['seconds']
        timestamp_proto.nanos = timestamp['nanos']
        return timestamp_proto

    @staticmethod
    def _timestamp_from_proto(timestamp_proto):
        return {
            "seconds": timestamp_proto.seconds,
            "nanos": timestamp_proto.nanos
        }
