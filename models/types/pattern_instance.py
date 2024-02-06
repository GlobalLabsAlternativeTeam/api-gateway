class PatternInstance:
    def __init__(self, instance_id=None, status=None, pattern_id=None, author_id=None, pattern_name=None, created_at=None, updated_at=None, deleted_at=None, tasks=None):
        self.instance_id = instance_id
        self.status = status
        self.pattern_id = pattern_id
        self.author_id = author_id
        self.pattern_name = pattern_name
        self.created_at = created_at
        self.updated_at = updated_at
        self.deleted_at = deleted_at
        self.tasks = tasks or []