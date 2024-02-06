class Task:
    def __init__(self, id=None, level=None, name=None, status=None, blockedBy=None, responsible=None, timeLimit=None, children=None, comment=None):
        self.id = id
        self.level = level
        self.name = name
        self.status = status
        self.blocked_by = blockedBy or []
        self.responsible = responsible
        self.time_limit = timeLimit
        self.children = children or []
        self.comment = comment