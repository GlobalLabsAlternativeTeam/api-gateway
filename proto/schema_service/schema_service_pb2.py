# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/schema_service/schema_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)proto/schema_service/schema_service.proto\x12\x17\x61lt_team.schema_service\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\"k\n\x13\x43reateSchemaRequest\x12\x11\n\tauthor_id\x18\x01 \x01(\t\x12\x13\n\x0bschema_name\x18\x02 \x01(\t\x12,\n\x05tasks\x18\x03 \x03(\x0b\x32\x1d.alt_team.schema_service.Task\"G\n\x14\x43reateSchemaResponse\x12/\n\x06schema\x18\x01 \x01(\x0b\x32\x1f.alt_team.schema_service.Schema\"\x16\n\x14GetAllSchemasRequest\"I\n\x15GetAllSchemasResponse\x12\x30\n\x07schemas\x18\x01 \x03(\x0b\x32\x1f.alt_team.schema_service.Schema\")\n\x14GetSchemaByIDRequest\x12\x11\n\tschema_id\x18\x01 \x01(\t\"[\n\x15GetSchemaByIDResponse\x12\x11\n\tschema_id\x18\x01 \x01(\t\x12/\n\x06schema\x18\x02 \x01(\x0b\x32\x1f.alt_team.schema_service.Schema\",\n\x17\x44\x65leteSchemaByIDRequest\x12\x11\n\tschema_id\x18\x01 \x01(\t\"-\n\x18\x44\x65leteSchemaByIDResponse\x12\x11\n\tschema_id\x18\x01 \x01(\t\"\x81\x02\n\x06Schema\x12\x11\n\tschema_id\x18\x01 \x01(\t\x12\x11\n\tauthor_id\x18\x02 \x01(\t\x12\x13\n\x0bschema_name\x18\x03 \x01(\t\x12.\n\ncreated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\ndeleted_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x05tasks\x18\x07 \x03(\x0b\x32\x1d.alt_team.schema_service.Task\"\x81\x02\n\x04Task\x12\n\n\x02id\x18\x01 \x01(\x03\x12\r\n\x05level\x18\x02 \x01(\x05\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x33\n\x06status\x18\x04 \x01(\x0e\x32#.alt_team.schema_service.TaskStatus\x12\x12\n\nblocked_by\x18\x05 \x03(\x03\x12\x13\n\x0bresponsible\x18\x06 \x01(\t\x12\x12\n\ntime_limit\x18\x07 \x01(\x03\x12/\n\x08\x63hildren\x18\x08 \x03(\x0b\x32\x1d.alt_team.schema_service.Task\x12-\n\x07\x63omment\x18\t \x01(\x0b\x32\x1c.google.protobuf.StringValue*\x92\x01\n\nTaskStatus\x12\x1b\n\x17TASK_STATUS_UNSPECIFIED\x10\x00\x12\x1b\n\x17TASK_STATUS_NOT_STARTED\x10\x01\x12\x1b\n\x17TASK_STATUS_IN_PROGRESS\x10\x02\x12\x17\n\x13TASK_STATUS_BLOCKED\x10\x03\x12\x14\n\x10TASK_STATUS_DONE\x10\x04\x32\xd5\x03\n\rSchemaService\x12k\n\x0c\x43reateSchema\x12,.alt_team.schema_service.CreateSchemaRequest\x1a-.alt_team.schema_service.CreateSchemaResponse\x12n\n\rGetAllSchemas\x12-.alt_team.schema_service.GetAllSchemasRequest\x1a..alt_team.schema_service.GetAllSchemasResponse\x12n\n\rGetSchemaByID\x12-.alt_team.schema_service.GetSchemaByIDRequest\x1a..alt_team.schema_service.GetSchemaByIDResponse\x12w\n\x10\x44\x65leteSchemaByID\x12\x30.alt_team.schema_service.DeleteSchemaByIDRequest\x1a\x31.alt_team.schema_service.DeleteSchemaByIDResponseB\x12Z\x10./schema_serviceb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.schema_service.schema_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\020./schema_service'
  _globals['_TASKSTATUS']._serialized_start=1166
  _globals['_TASKSTATUS']._serialized_end=1312
  _globals['_CREATESCHEMAREQUEST']._serialized_start=135
  _globals['_CREATESCHEMAREQUEST']._serialized_end=242
  _globals['_CREATESCHEMARESPONSE']._serialized_start=244
  _globals['_CREATESCHEMARESPONSE']._serialized_end=315
  _globals['_GETALLSCHEMASREQUEST']._serialized_start=317
  _globals['_GETALLSCHEMASREQUEST']._serialized_end=339
  _globals['_GETALLSCHEMASRESPONSE']._serialized_start=341
  _globals['_GETALLSCHEMASRESPONSE']._serialized_end=414
  _globals['_GETSCHEMABYIDREQUEST']._serialized_start=416
  _globals['_GETSCHEMABYIDREQUEST']._serialized_end=457
  _globals['_GETSCHEMABYIDRESPONSE']._serialized_start=459
  _globals['_GETSCHEMABYIDRESPONSE']._serialized_end=550
  _globals['_DELETESCHEMABYIDREQUEST']._serialized_start=552
  _globals['_DELETESCHEMABYIDREQUEST']._serialized_end=596
  _globals['_DELETESCHEMABYIDRESPONSE']._serialized_start=598
  _globals['_DELETESCHEMABYIDRESPONSE']._serialized_end=643
  _globals['_SCHEMA']._serialized_start=646
  _globals['_SCHEMA']._serialized_end=903
  _globals['_TASK']._serialized_start=906
  _globals['_TASK']._serialized_end=1163
  _globals['_SCHEMASERVICE']._serialized_start=1315
  _globals['_SCHEMASERVICE']._serialized_end=1784
# @@protoc_insertion_point(module_scope)
