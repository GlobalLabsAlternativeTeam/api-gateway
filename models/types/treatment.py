

class Treatment:
    def __init__(self, treatment_id=None, doctor_id=None, patient_id=None, status=None, pattern_instance=None, started_at=None, finished_at=None, deleted_at=None):
        self.treatment_id = treatment_id
        self.doctor_id = doctor_id
        self.patient_id = patient_id
        self.status = status
        self.pattern_instance = pattern_instance
        self.started_at = started_at
        self.finished_at = finished_at
        self.deleted_at = deleted_at