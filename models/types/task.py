from task_status import TaskStatus

class Task:
    def __init__(self, id, level, name, status, blocked_by, responsible, time_limit, children, comment):
        self.id = id
        self.level = level
        self.name = name
        self.status = status
        self.blocked_by = blocked_by
        self.responsible = responsible
        self.time_limit = time_limit
        self.children = children
        self.comment = Comment(comment)

    def to_json(self):
        return {
            "id": self.id,
            "level": self.level,
            "name": self.name,
            "status": self.status,
            "blocked_by": self.blocked_by,
            "responsible": self.responsible,
            "time_limit": self.time_limit,
            "children": self.children,
            "comment": {"value": self.comment.value}
        }

    def to_dict(self):
        return self.to_json()

    @classmethod
    def from_json(cls, json_data):
        return cls(
            json_data["id"],
            json_data["level"],
            json_data["name"],
            json_data["status"],
            json_data["blocked_by"],
            json_data["responsible"],
            json_data["time_limit"],
            json_data["children"],
            json_data["comment"]["value"]
        )

    @classmethod
    def from_dict(cls, dict_data):
        return cls.from_json(dict_data)

    @classmethod
    def from_proto(cls, proto_data):
        comment_value = proto_data.comment.value if proto_data.HasField("comment") else ""
        return cls(
            proto_data.id,
            proto_data.level,
            proto_data.name,
            TaskStatus(proto_data.status),
            proto_data.blocked_by,
            proto_data.responsible if proto_data.HasField("responsible") else None,
            proto_data.time_limit if proto_data.HasField("time_limit") else None,
            [cls.from_proto(child) for child in proto_data.children],
            comment_value
        )


class Comment:
    def __init__(self, value):
        self.value = value
