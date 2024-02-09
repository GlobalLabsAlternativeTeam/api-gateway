import grpc

import vars
from interfaces.user import UserInterFace

# from grpc.process_execution_service import service__pb2_grpc, service__pb2
from proto.process_execution_service import service_pb2, service_pb2_grpc


class User(UserInterFace):
    def __init__(self):
        super(UserInterFace, self).__init__()
        self.execution_serice = grpc.insecure_channel(
            f'''localhost:{vars.EXECUTION_SERVICE_PORT}''')
        self.execution_service_stub = service_pb2_grpc.ProcessExecutionServiceStub(
            self.execution_serice)

    def GetUsers(self, context):
        pass
