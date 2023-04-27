# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: secretflow/protos/kuscia/kuscia_task.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='secretflow/protos/kuscia/kuscia_task.proto',
  package='secretflow.kuscia',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n*secretflow/protos/kuscia/kuscia_task.proto\x12\x11secretflow.kuscia\"/\n\x07Service\x12\x11\n\tport_name\x18\x01 \x01(\t\x12\x11\n\tendpoints\x18\x02 \x03(\t\"Q\n\x05Party\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04role\x18\x02 \x01(\t\x12,\n\x08services\x18\x03 \x03(\x0b\x32\x1a.secretflow.kuscia.Service\"m\n\rClusterDefine\x12)\n\x07parties\x18\x01 \x03(\x0b\x32\x18.secretflow.kuscia.Party\x12\x16\n\x0eself_party_idx\x18\x02 \x01(\x05\x12\x19\n\x11self_endpoint_idx\x18\x03 \x01(\x05\"C\n\x04Port\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\x05\x12\r\n\x05scope\x18\x03 \x01(\t\x12\x10\n\x08protocol\x18\x04 \x01(\t\"8\n\x0e\x41llocatedPorts\x12&\n\x05ports\x18\x01 \x03(\x0b\x32\x17.secretflow.kuscia.Portb\x06proto3'
)




_SERVICE = _descriptor.Descriptor(
  name='Service',
  full_name='secretflow.kuscia.Service',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='port_name', full_name='secretflow.kuscia.Service.port_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='endpoints', full_name='secretflow.kuscia.Service.endpoints', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=65,
  serialized_end=112,
)


_PARTY = _descriptor.Descriptor(
  name='Party',
  full_name='secretflow.kuscia.Party',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='secretflow.kuscia.Party.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='role', full_name='secretflow.kuscia.Party.role', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='services', full_name='secretflow.kuscia.Party.services', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=114,
  serialized_end=195,
)


_CLUSTERDEFINE = _descriptor.Descriptor(
  name='ClusterDefine',
  full_name='secretflow.kuscia.ClusterDefine',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='parties', full_name='secretflow.kuscia.ClusterDefine.parties', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='self_party_idx', full_name='secretflow.kuscia.ClusterDefine.self_party_idx', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='self_endpoint_idx', full_name='secretflow.kuscia.ClusterDefine.self_endpoint_idx', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=197,
  serialized_end=306,
)


_PORT = _descriptor.Descriptor(
  name='Port',
  full_name='secretflow.kuscia.Port',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='secretflow.kuscia.Port.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='port', full_name='secretflow.kuscia.Port.port', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='scope', full_name='secretflow.kuscia.Port.scope', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='protocol', full_name='secretflow.kuscia.Port.protocol', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=308,
  serialized_end=375,
)


_ALLOCATEDPORTS = _descriptor.Descriptor(
  name='AllocatedPorts',
  full_name='secretflow.kuscia.AllocatedPorts',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ports', full_name='secretflow.kuscia.AllocatedPorts.ports', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=377,
  serialized_end=433,
)

_PARTY.fields_by_name['services'].message_type = _SERVICE
_CLUSTERDEFINE.fields_by_name['parties'].message_type = _PARTY
_ALLOCATEDPORTS.fields_by_name['ports'].message_type = _PORT
DESCRIPTOR.message_types_by_name['Service'] = _SERVICE
DESCRIPTOR.message_types_by_name['Party'] = _PARTY
DESCRIPTOR.message_types_by_name['ClusterDefine'] = _CLUSTERDEFINE
DESCRIPTOR.message_types_by_name['Port'] = _PORT
DESCRIPTOR.message_types_by_name['AllocatedPorts'] = _ALLOCATEDPORTS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Service = _reflection.GeneratedProtocolMessageType('Service', (_message.Message,), {
  'DESCRIPTOR' : _SERVICE,
  '__module__' : 'secretflow.protos.kuscia.kuscia_task_pb2'
  # @@protoc_insertion_point(class_scope:secretflow.kuscia.Service)
  })
_sym_db.RegisterMessage(Service)

Party = _reflection.GeneratedProtocolMessageType('Party', (_message.Message,), {
  'DESCRIPTOR' : _PARTY,
  '__module__' : 'secretflow.protos.kuscia.kuscia_task_pb2'
  # @@protoc_insertion_point(class_scope:secretflow.kuscia.Party)
  })
_sym_db.RegisterMessage(Party)

ClusterDefine = _reflection.GeneratedProtocolMessageType('ClusterDefine', (_message.Message,), {
  'DESCRIPTOR' : _CLUSTERDEFINE,
  '__module__' : 'secretflow.protos.kuscia.kuscia_task_pb2'
  # @@protoc_insertion_point(class_scope:secretflow.kuscia.ClusterDefine)
  })
_sym_db.RegisterMessage(ClusterDefine)

Port = _reflection.GeneratedProtocolMessageType('Port', (_message.Message,), {
  'DESCRIPTOR' : _PORT,
  '__module__' : 'secretflow.protos.kuscia.kuscia_task_pb2'
  # @@protoc_insertion_point(class_scope:secretflow.kuscia.Port)
  })
_sym_db.RegisterMessage(Port)

AllocatedPorts = _reflection.GeneratedProtocolMessageType('AllocatedPorts', (_message.Message,), {
  'DESCRIPTOR' : _ALLOCATEDPORTS,
  '__module__' : 'secretflow.protos.kuscia.kuscia_task_pb2'
  # @@protoc_insertion_point(class_scope:secretflow.kuscia.AllocatedPorts)
  })
_sym_db.RegisterMessage(AllocatedPorts)


# @@protoc_insertion_point(module_scope)