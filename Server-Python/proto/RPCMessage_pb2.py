# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: RPCMessage.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='RPCMessage.proto',
  package='',
  serialized_pb='\n\x10RPCMessage.proto\"D\n\x0eRPCRequest_pb2\x12\x0e\n\x06\x63\x61llid\x18\x01 \x02(\x05\x12\x12\n\nmethodName\x18\x02 \x02(\t\x12\x0e\n\x06params\x18\x03 \x02(\x0c\"3\n\x0fRPCResponse_pb2\x12\x0e\n\x06\x63\x61llid\x18\x01 \x02(\x05\x12\x10\n\x08retvalue\x18\x02 \x02(\x0c')




_RPCREQUEST_PB2 = _descriptor.Descriptor(
  name='RPCRequest_pb2',
  full_name='RPCRequest_pb2',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='callid', full_name='RPCRequest_pb2.callid', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='methodName', full_name='RPCRequest_pb2.methodName', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='params', full_name='RPCRequest_pb2.params', index=2,
      number=3, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=20,
  serialized_end=88,
)


_RPCRESPONSE_PB2 = _descriptor.Descriptor(
  name='RPCResponse_pb2',
  full_name='RPCResponse_pb2',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='callid', full_name='RPCResponse_pb2.callid', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='retvalue', full_name='RPCResponse_pb2.retvalue', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=90,
  serialized_end=141,
)

DESCRIPTOR.message_types_by_name['RPCRequest_pb2'] = _RPCREQUEST_PB2
DESCRIPTOR.message_types_by_name['RPCResponse_pb2'] = _RPCRESPONSE_PB2

class RPCRequest_pb2(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RPCREQUEST_PB2

  # @@protoc_insertion_point(class_scope:RPCRequest_pb2)

class RPCResponse_pb2(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RPCRESPONSE_PB2

  # @@protoc_insertion_point(class_scope:RPCResponse_pb2)


# @@protoc_insertion_point(module_scope)
