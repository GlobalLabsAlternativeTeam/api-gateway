import grpc

import vars
from interfaces.schema import SchemaInterface



class Schema(SchemaInterface):
    def __init__(self):
        pass

    def GetSchema(self, context, schema_id):
        return super().GetSchema(context, schema_id)
    

    def GetSchemas(self, context):
        return super().GetSchemas(context)
    
    def CreateSchema(self, context, schema):
        return super().CreateSchema(context, schema)
    
    def UpdateSchema(self, context, schema):
        return super().UpdateSchema(context, schema)