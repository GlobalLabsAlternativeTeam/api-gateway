import grpc

import vars
import service.schema_service_converter as converter
from interfaces.schema import SchemaInterface

from proto.schema_service import schema_service_pb2, schema_service_pb2_grpc

class Schema(SchemaInterface):
    def __init__(self):
        super(SchemaInterface, self).__init__()
        self.schema_service = grpc.insecure_channel(f'''localhost:{vars.SCHEMA_SERVICE_PORT}''', options=(('grpc.enable_http_proxy', 0),))
        self.schema_service_stub = schema_service_pb2_grpc.SchemaServiceStub(self.schema_service)

    def GetSchema(self, context, schema_id):
        print("START GetSchema Schema")
        request = schema_service_pb2.GetSchemaByIDRequest(schema_id = schema_id)
        try:
            response = self.schema_service_stub.GetSchemaByID(request)
            print("END GetSchema Schema")
            return {"schema" : response,
                    "error": ""
                    }
            
        except grpc._channel._InactiveRpcError as e:
            status_code = e.code()
            details = e.details()
            
            if status_code == grpc.StatusCode.UNKNOWN:
                # Extracting grpc_message
                return   {"schema" : '',
                    "error": details
                    }
            else:
                # Handle other status codes if needed
                print("Unexpected gRPC error:", e)
                return {"schema" : '',
                    "error": e
                    }
        

    def GetSchemas(self, context):
        return super().GetSchemas(context)
    
    def CreateSchema(self, context, tasks, author_id, schema_name):
        print("START CreateSchema Schema")
        grpc_tasks = []
        for task in tasks:
            grpc_tasks.append(converter.TaskToGrpc(task))

        # TODO: Validate Task schema
        request = schema_service_pb2.CreateSchemaRequest(author_id = author_id,
                                                         schema_name = schema_name,
                                                         tasks = grpc_tasks)
        try:
            response = self.schema_service_stub.CreateSchema(request)
            print("END CreateSchema Schema")
            return {"schema" : response,
                    "error": ""
                    }
            
        except grpc._channel._InactiveRpcError as e:
            status_code = e.code()
            details = e.details()
            
            if status_code == grpc.StatusCode.UNKNOWN:
                # Extracting grpc_message
                return   {"schema" : '',
                    "error": details
                    }
            else:
                # Handle other status codes if needed
                print("Unexpected gRPC error:", e)
                return {"schema" : '',
                    "error": e
                    }
    
    def UpdateSchema(self, context, schema):
        return super().UpdateSchema(context, schema)