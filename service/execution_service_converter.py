import json
from google.protobuf.timestamp_pb2 import Timestamp
from proto.schema_service import schema_service_pb2, schema_service_pb2_grpc
from proto.process_execution_service import service_pb2, service_pb2_grpc
from google.protobuf.wrappers_pb2 import StringValue

import grpc


def SchemaToGrpc(schema):
    grpc_tasks = []
    for task in schema['tasks']:
        grpc_tasks.append(TaskToGrpc(task))
    created_at = Timestamp()
    created_at.FromJsonString(schema['createdAt'])
    updated_at = Timestamp()
    updated_at.FromJsonString(schema['updatedAt'])
    deleted_at = Timestamp()
    deleted_at.FromJsonString(schema['deletedAt'])
    grpc_schema = service_pb2.Schema(
        schema_id = schema['schemaId'],
        author_id = schema['authorId'],
        schema_name = schema['schemaName'],
        created_at = created_at,
        updated_at = updated_at,
        deleted_at = deleted_at,
        tasks= grpc_tasks
    )

    return grpc_schema


def TaskToGrpc(task_data):
    if isinstance(task_data, dict):
        comment = task_data['comment']
        comment_value = StringValue(value=comment)
        children = task_data.get('children', [])
        grpc_children = [TaskToGrpc(task) for task in children]
        task = service_pb2.Task(
            id=int(task_data.get('id', '0')),
            level=int(task_data.get('level', '0')),
            name=task_data['name'],
            status=service_pb2.TaskStatus.Value(task_data.get('status', 'TASK_STATUS_UNSPECIFIED')),
            # TODO: Add normal recast
            blocked_by=[int(task_id) for task_id in task_data.get('blockedBy', [])],
            responsible=task_data.get('responsible', ''),
            time_limit=int(task_data.get('timeLimit', '0')),
            children=grpc_children,
            comment=comment_value
        )
        return task
    else:
        print(f"Task data is not a dictionary: {task_data}")
        return None
