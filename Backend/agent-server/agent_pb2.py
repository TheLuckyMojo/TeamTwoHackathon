# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: agent.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='agent.proto',
  package='agent',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0b\x61gent.proto\x12\x05\x61gent\"[\n\x10OperatingPicture\x12\x13\n\x0bnumMissiles\x18\x01 \x01(\x05\x12\x32\n\x10targetIdToDamage\x18\x02 \x01(\x0b\x32\x18.agent.TargetToDamageMap\"3\n\x15TargetIdToDamageEntry\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x61mage\x18\x02 \x01(\x05\"B\n\x11TargetToDamageMap\x12-\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x1c.agent.TargetIdToDamageEntry\"D\n\x0ePlanAssessment\x12\x32\n\x11\x61\x63tionAssessments\x18\x01 \x03(\x0b\x32\x17.agent.ActionAssessment\"\xb9\x01\n\x10\x41\x63tionAssessment\x12\x16\n\x0e\x61\x63tionTargetId\x18\x01 \x01(\t\x12\x17\n\x0fnumMissilesLeft\x18\x02 \x01(\x05\x12\x39\n\x17targetIdToCurrentDamage\x18\x03 \x01(\x0b\x32\x18.agent.TargetToDamageMap\x12\x39\n\x17targetIdToDesiredDamage\x18\x04 \x01(\x0b\x32\x18.agent.TargetToDamageMap2N\n\x05\x41gent\x12\x45\n\x11GetPlanAssessment\x12\x17.agent.OperatingPicture\x1a\x15.agent.PlanAssessment\"\x00\x62\x06proto3'
)




_OPERATINGPICTURE = _descriptor.Descriptor(
  name='OperatingPicture',
  full_name='agent.OperatingPicture',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='numMissiles', full_name='agent.OperatingPicture.numMissiles', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='targetIdToDamage', full_name='agent.OperatingPicture.targetIdToDamage', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=22,
  serialized_end=113,
)


_TARGETIDTODAMAGEENTRY = _descriptor.Descriptor(
  name='TargetIdToDamageEntry',
  full_name='agent.TargetIdToDamageEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='agent.TargetIdToDamageEntry.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='damage', full_name='agent.TargetIdToDamageEntry.damage', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=115,
  serialized_end=166,
)


_TARGETTODAMAGEMAP = _descriptor.Descriptor(
  name='TargetToDamageMap',
  full_name='agent.TargetToDamageMap',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='entries', full_name='agent.TargetToDamageMap.entries', index=0,
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
  serialized_start=168,
  serialized_end=234,
)


_PLANASSESSMENT = _descriptor.Descriptor(
  name='PlanAssessment',
  full_name='agent.PlanAssessment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='actionAssessments', full_name='agent.PlanAssessment.actionAssessments', index=0,
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
  serialized_start=236,
  serialized_end=304,
)


_ACTIONASSESSMENT = _descriptor.Descriptor(
  name='ActionAssessment',
  full_name='agent.ActionAssessment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='actionTargetId', full_name='agent.ActionAssessment.actionTargetId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='numMissilesLeft', full_name='agent.ActionAssessment.numMissilesLeft', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='targetIdToCurrentDamage', full_name='agent.ActionAssessment.targetIdToCurrentDamage', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='targetIdToDesiredDamage', full_name='agent.ActionAssessment.targetIdToDesiredDamage', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=307,
  serialized_end=492,
)

_OPERATINGPICTURE.fields_by_name['targetIdToDamage'].message_type = _TARGETTODAMAGEMAP
_TARGETTODAMAGEMAP.fields_by_name['entries'].message_type = _TARGETIDTODAMAGEENTRY
_PLANASSESSMENT.fields_by_name['actionAssessments'].message_type = _ACTIONASSESSMENT
_ACTIONASSESSMENT.fields_by_name['targetIdToCurrentDamage'].message_type = _TARGETTODAMAGEMAP
_ACTIONASSESSMENT.fields_by_name['targetIdToDesiredDamage'].message_type = _TARGETTODAMAGEMAP
DESCRIPTOR.message_types_by_name['OperatingPicture'] = _OPERATINGPICTURE
DESCRIPTOR.message_types_by_name['TargetIdToDamageEntry'] = _TARGETIDTODAMAGEENTRY
DESCRIPTOR.message_types_by_name['TargetToDamageMap'] = _TARGETTODAMAGEMAP
DESCRIPTOR.message_types_by_name['PlanAssessment'] = _PLANASSESSMENT
DESCRIPTOR.message_types_by_name['ActionAssessment'] = _ACTIONASSESSMENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OperatingPicture = _reflection.GeneratedProtocolMessageType('OperatingPicture', (_message.Message,), {
  'DESCRIPTOR' : _OPERATINGPICTURE,
  '__module__' : 'agent_pb2'
  # @@protoc_insertion_point(class_scope:agent.OperatingPicture)
  })
_sym_db.RegisterMessage(OperatingPicture)

TargetIdToDamageEntry = _reflection.GeneratedProtocolMessageType('TargetIdToDamageEntry', (_message.Message,), {
  'DESCRIPTOR' : _TARGETIDTODAMAGEENTRY,
  '__module__' : 'agent_pb2'
  # @@protoc_insertion_point(class_scope:agent.TargetIdToDamageEntry)
  })
_sym_db.RegisterMessage(TargetIdToDamageEntry)

TargetToDamageMap = _reflection.GeneratedProtocolMessageType('TargetToDamageMap', (_message.Message,), {
  'DESCRIPTOR' : _TARGETTODAMAGEMAP,
  '__module__' : 'agent_pb2'
  # @@protoc_insertion_point(class_scope:agent.TargetToDamageMap)
  })
_sym_db.RegisterMessage(TargetToDamageMap)

PlanAssessment = _reflection.GeneratedProtocolMessageType('PlanAssessment', (_message.Message,), {
  'DESCRIPTOR' : _PLANASSESSMENT,
  '__module__' : 'agent_pb2'
  # @@protoc_insertion_point(class_scope:agent.PlanAssessment)
  })
_sym_db.RegisterMessage(PlanAssessment)

ActionAssessment = _reflection.GeneratedProtocolMessageType('ActionAssessment', (_message.Message,), {
  'DESCRIPTOR' : _ACTIONASSESSMENT,
  '__module__' : 'agent_pb2'
  # @@protoc_insertion_point(class_scope:agent.ActionAssessment)
  })
_sym_db.RegisterMessage(ActionAssessment)



_AGENT = _descriptor.ServiceDescriptor(
  name='Agent',
  full_name='agent.Agent',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=494,
  serialized_end=572,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetPlanAssessment',
    full_name='agent.Agent.GetPlanAssessment',
    index=0,
    containing_service=None,
    input_type=_OPERATINGPICTURE,
    output_type=_PLANASSESSMENT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_AGENT)

DESCRIPTOR.services_by_name['Agent'] = _AGENT

# @@protoc_insertion_point(module_scope)
