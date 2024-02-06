class Task:
    def __init__(self, id=None, level=None, name=None, status=None, blocked_by=None, responsible=None, time_limit=None, children=None, comment=None):
        self.id = id
        self.level = level
        self.name = name
        self.status = status
        self.blocked_by = blocked_by or []
        self.responsible = responsible
        self.time_limit = time_limit
        self.children = children or []
        self.comment = comment