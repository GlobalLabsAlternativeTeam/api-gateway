import grpc

import vars
from interfaces.instance import InstaceInterface
import service.execution_service_converter as converter
# from grpc.process_execution_service import service__pb2_grpc, service__pb2
from proto.process_execution_service import service_pb2, service_pb2_grpc

class Instance(InstaceInterface):
    def __init__(self):
        super(InstaceInterface, self).__init__()
        self.execution_serice = grpc.insecure_channel(f'''localhost:{vars.EXECUTION_SERVICE_PORT}''')
        self.execution_service_stub = service_pb2_grpc.ProcessExecutionServiceStub(self.execution_serice)
    
    def GetInstances(self, patient_id):
        print("START GetInstances Instance")
        request = service_pb2.GetTreatmentsByPatientIDRequest(patient_id = patient_id)
        response = self.execution_service_stub.GetTreatmentsByPatientID(request)
        print("END GetInstances Instance")
        return response

    def GetInstance(self, instance_id):
        print("START GetInstance Instance")
        request = service_pb2.GetTreatmentByIDRequest(treatment_id = instance_id)
        response = self.execution_service_stub.GetTreatmentByID(request)
        print("END GetInstance Instance")
        return response

    def GetPatients(self, doctor_id):
        print("START GetPatients Instance")
        request = service_pb2.GetPatientsByDoctorIDRequest(doctor_id = doctor_id)
        response = self.execution_service_stub.GetPatientsByDoctorID(request)
        print("END GetPatients Instance")
        return response
        
    def CompleteTasks(self, instance_id, task_ids):
        print("START CompleteTasks Instance")
        request = service_pb2.CompleteTasksRequest(instance_id = instance_id, task_ids = task_ids)
        response = self.execution_service_stub.CompleteTasks(request)
        print("END CompleteTasks Instance")
        return response
    
    def CreateTreatment(self, schema, patient_id, doctor_id):
        print("START CreateTreatment Instance")
        grpc_schema = converter.SchemaToGrpc(schema)
        request = service_pb2.CreateTreatmentRequest(schema = grpc_schema, patient_id = patient_id, doctor_id = doctor_id)

        try:
            response = self.execution_service_stub.CreateTreatment(request)
            print("END CreateTreatment Schema")
            return {"treatment" : response,
                    "error": ""
                    }
            
        except grpc._channel._InactiveRpcError as e:
            status_code = e.code()
            details = e.details()
            
            if status_code == grpc.StatusCode.UNKNOWN:
                # Extracting grpc_message
                return   {"treatment" : '',
                    "error": details
                    }
            else:
                # Handle other status codes if needed
                print("Unexpected gRPC error:", e)
                return {"treatment" : '',
                    "error": e
                    }