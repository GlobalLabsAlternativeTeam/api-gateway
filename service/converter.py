import json
from google.protobuf.timestamp_pb2 import Timestamp
from proto.schema_service import schema_service_pb2, schema_service_pb2_grpc

import grpc

def TaskToGrpc(tasks):
    grpc_tasks = []
    for task_data in tasks:
        task = schema_service_pb2.Task(
            id=task_data['id'],
            level=task_data['level'],
            name=task_data['name'],
            status=schema_service_pb2.TaskStatus.Value(task_data['status']),
            # TODO: Add normal recast
            blocked_by=task_data['blocked_by'],
            responsible=task_data['responsible'],
            time_limit=task_data['time_limit'],
            children=[schema_service_pb2.Task(name=name) for name in task_data['children']],
            comment=task_data['comment']
        )
        grpc_tasks.append(task)
    return grpc_tasks

