from enum import Enum

class TaskStatus(Enum):
    STATUS_UNSPECIFIED = 0
    STATUS_NOT_STARTED = 1
    STATUS_IN_PROGRESS = 2
    STATUS_BLOCKED = 3
    STATUS_DONE = 4
