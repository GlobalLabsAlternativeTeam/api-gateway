import grpc

import vars
from interfaces.instance import InstaceInterface

# from grpc.process_execution_service import service__pb2_grpc, service__pb2
from proto.process_execution_service import service_pb2, service_pb2_grpc

class Instance(InstaceInterface):
    def __init__(self):
        super(InstaceInterface, self).__init__()
        self.execution_serice = grpc.insecure_channel(f'''localhost:{vars.EXECUTION_SERVICE_PORT}''')
        self.execution_service_stub = service_pb2_grpc.ProcessExecutionServiceStub(self.execution_serice)

    
    def GetInstances(self, patient_id):
        request = service_pb2.GetInstancesByPatientReq(patient_id = int(patient_id))
        response = self.execution_service_stub.GetInstancesByPatient(request)
        # print(f'''response: {response}''')
        return response

    def GetInstance(self, context, instance_id):
        pass

    def GetInstaceStatus(self, context, instance_id):
        pass

    def GetTask(self, context, instance_id, task_id):
        pass

    def IfTaskIsLocked(self, context, instance_id, task_id):
        pass

    def GetTaskStatus(self, context, instance_id, task_id):
        pass

    def CreateInstance(self, context, schema, patient_id, doctor_id):
        pass