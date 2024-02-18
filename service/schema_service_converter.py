import json
from google.protobuf.timestamp_pb2 import Timestamp
from proto.schema_service import schema_service_pb2, schema_service_pb2_grpc
from proto.process_execution_service import service_pb2, service_pb2_grpc
from google.protobuf.wrappers_pb2 import StringValue

import grpc

def TaskToGrpc(task_data):
    if isinstance(task_data, dict):

        comment = task_data['comment']['value']
        comment_value = StringValue(value=comment)
        children = task_data.get('children', [])
        grpc_children = [TaskToGrpc(task) for task in children]
        task = schema_service_pb2.Task(
            id=task_data['id'],
            level=task_data['level'],
            name=task_data['name'],
            status=schema_service_pb2.TaskStatus.Value(task_data['status']),
            # TODO: Add normal recast
            blocked_by=task_data['blocked_by'],
            responsible=task_data['responsible'],
            time_limit=task_data['time_limit'],
            children=grpc_children,
            comment=comment_value
        )
        return task
    else:
        print(f"Task data is not a dictionary: {task_data}")
        return None
