import grpc

import vars
from interfaces.instance import InstaceInterface

# from grpc.process_execution_service import service__pb2_grpc, service__pb2
from proto.process_execution_service import service_pb2, service_pb2_grpc

class Instance(InstaceInterface):
    def __init__(self):
        super(InstaceInterface, self).__init__()
        # self.GetInstances()
        # self.GetInstance()
        # self.GetInstaceStatus()
        # self.GetTask()
        # self.IfTaskIsLocked()
        # self.GetTaskStatus()
        # pass

    
    def GetInstances(self, patient_id):
        execution_serice = grpc.insecure_channel(f'''localhost:{vars.EXECUTION_SERVICE_PORT}''')
        execution_service_stub = service_pb2_grpc.ProcessExecutionServiceStub(execution_serice)
        request = service_pb2.GetInstancesByPatientReq(patient_id = int(patient_id))
        response = execution_service_stub.GetInstancesByPatient(request)
        print(f'''response: {response}''')
        # print(f'''code: {response.keys()}''')
        return response

    def GetInstance(self):
        pass

    def GetInstaceStatus(self):
        pass

    def GetTask(self):
        pass

    def GetTask(self):
        pass

    def IfTaskIsLocked(self):
        pass

    def GetTaskStatus(self):
        pass