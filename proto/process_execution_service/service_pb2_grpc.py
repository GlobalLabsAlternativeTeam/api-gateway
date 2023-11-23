# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from proto.process_execution_service import service_pb2 as proto_dot_process__execution__service_dot_service__pb2


class ProcessExecutionServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateInstance = channel.unary_unary(
                '/treatment.ProcessExecutionService/CreateInstance',
                request_serializer=proto_dot_process__execution__service_dot_service__pb2.CreateInstanceReq.SerializeToString,
                response_deserializer=proto_dot_process__execution__service_dot_service__pb2.Instance.FromString,
                )
        self.GetInstancesByPatient = channel.unary_stream(
                '/treatment.ProcessExecutionService/GetInstancesByPatient',
                request_serializer=proto_dot_process__execution__service_dot_service__pb2.GetInstancesByPatientReq.SerializeToString,
                response_deserializer=proto_dot_process__execution__service_dot_service__pb2.Instance.FromString,
                )
        self.GetInstanceById = channel.unary_unary(
                '/treatment.ProcessExecutionService/GetInstanceById',
                request_serializer=proto_dot_process__execution__service_dot_service__pb2.GetInstanceByIdReq.SerializeToString,
                response_deserializer=proto_dot_process__execution__service_dot_service__pb2.Instance.FromString,
                )
        self.CompleteTask = channel.unary_stream(
                '/treatment.ProcessExecutionService/CompleteTask',
                request_serializer=proto_dot_process__execution__service_dot_service__pb2.CompleteTaskReq.SerializeToString,
                response_deserializer=proto_dot_process__execution__service_dot_service__pb2.TaskStatusGroup.FromString,
                )
        self.GetTask = channel.unary_stream(
                '/treatment.ProcessExecutionService/GetTask',
                request_serializer=proto_dot_process__execution__service_dot_service__pb2.GetTaskReq.SerializeToString,
                response_deserializer=proto_dot_process__execution__service_dot_service__pb2.Task.FromString,
                )
        self.GetSchemaInstance = channel.unary_unary(
                '/treatment.ProcessExecutionService/GetSchemaInstance',
                request_serializer=proto_dot_process__execution__service_dot_service__pb2.GetSchemaInstanceReq.SerializeToString,
                response_deserializer=proto_dot_process__execution__service_dot_service__pb2.SchemaInstance.FromString,
                )


class ProcessExecutionServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateInstance(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetInstancesByPatient(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetInstanceById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CompleteTask(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTask(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSchemaInstance(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProcessExecutionServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateInstance': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateInstance,
                    request_deserializer=proto_dot_process__execution__service_dot_service__pb2.CreateInstanceReq.FromString,
                    response_serializer=proto_dot_process__execution__service_dot_service__pb2.Instance.SerializeToString,
            ),
            'GetInstancesByPatient': grpc.unary_stream_rpc_method_handler(
                    servicer.GetInstancesByPatient,
                    request_deserializer=proto_dot_process__execution__service_dot_service__pb2.GetInstancesByPatientReq.FromString,
                    response_serializer=proto_dot_process__execution__service_dot_service__pb2.Instance.SerializeToString,
            ),
            'GetInstanceById': grpc.unary_unary_rpc_method_handler(
                    servicer.GetInstanceById,
                    request_deserializer=proto_dot_process__execution__service_dot_service__pb2.GetInstanceByIdReq.FromString,
                    response_serializer=proto_dot_process__execution__service_dot_service__pb2.Instance.SerializeToString,
            ),
            'CompleteTask': grpc.unary_stream_rpc_method_handler(
                    servicer.CompleteTask,
                    request_deserializer=proto_dot_process__execution__service_dot_service__pb2.CompleteTaskReq.FromString,
                    response_serializer=proto_dot_process__execution__service_dot_service__pb2.TaskStatusGroup.SerializeToString,
            ),
            'GetTask': grpc.unary_stream_rpc_method_handler(
                    servicer.GetTask,
                    request_deserializer=proto_dot_process__execution__service_dot_service__pb2.GetTaskReq.FromString,
                    response_serializer=proto_dot_process__execution__service_dot_service__pb2.Task.SerializeToString,
            ),
            'GetSchemaInstance': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSchemaInstance,
                    request_deserializer=proto_dot_process__execution__service_dot_service__pb2.GetSchemaInstanceReq.FromString,
                    response_serializer=proto_dot_process__execution__service_dot_service__pb2.SchemaInstance.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'treatment.ProcessExecutionService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ProcessExecutionService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateInstance(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/treatment.ProcessExecutionService/CreateInstance',
            proto_dot_process__execution__service_dot_service__pb2.CreateInstanceReq.SerializeToString,
            proto_dot_process__execution__service_dot_service__pb2.Instance.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetInstancesByPatient(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/treatment.ProcessExecutionService/GetInstancesByPatient',
            proto_dot_process__execution__service_dot_service__pb2.GetInstancesByPatientReq.SerializeToString,
            proto_dot_process__execution__service_dot_service__pb2.Instance.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetInstanceById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/treatment.ProcessExecutionService/GetInstanceById',
            proto_dot_process__execution__service_dot_service__pb2.GetInstanceByIdReq.SerializeToString,
            proto_dot_process__execution__service_dot_service__pb2.Instance.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CompleteTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/treatment.ProcessExecutionService/CompleteTask',
            proto_dot_process__execution__service_dot_service__pb2.CompleteTaskReq.SerializeToString,
            proto_dot_process__execution__service_dot_service__pb2.TaskStatusGroup.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/treatment.ProcessExecutionService/GetTask',
            proto_dot_process__execution__service_dot_service__pb2.GetTaskReq.SerializeToString,
            proto_dot_process__execution__service_dot_service__pb2.Task.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetSchemaInstance(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/treatment.ProcessExecutionService/GetSchemaInstance',
            proto_dot_process__execution__service_dot_service__pb2.GetSchemaInstanceReq.SerializeToString,
            proto_dot_process__execution__service_dot_service__pb2.SchemaInstance.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
