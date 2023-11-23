from service.instance import Instance

class API():
    def __init__(self):
        pass

    def get_patients(self, context, request):
        pass

    def get_instances(self, context, patient_id):
        instance = Instance()
        # patient_id = request.request.view_args('patient_id') 
        response = instance.GetInstances(patient_id)
        return response
        # pass

    def get_instance(self, context, request):
        pass

    def get_instance_status(self, context, request):
        pass

    def get_task(self, context, request):
        pass

    def is_task_locked(self, context, request):
        pass

    def get_task_status(self, context, request):
        pass

    def get_schemas(self, context, request):
        pass

    def get_schemas_by_doctor_id(self, context, request):
        pass
