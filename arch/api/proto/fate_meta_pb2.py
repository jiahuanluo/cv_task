#
#  Copyright 2019 The FATE Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fate-meta.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='fate-meta.proto',
  package='com.webank.ai.fate.api.core',
  syntax='proto3',
  serialized_options=_b('B\tBasicMeta'),
  serialized_pb=_b('\n\x0f\x66\x61te-meta.proto\x12\x1b\x63om.webank.ai.fate.api.core\"6\n\x08\x45ndpoint\x12\n\n\x02ip\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\x05\x12\x10\n\x08hostname\x18\x03 \x01(\t\"E\n\tEndpoints\x12\x38\n\tendpoints\x18\x01 \x03(\x0b\x32%.com.webank.ai.fate.api.core.Endpoint\"H\n\x04\x44\x61ta\x12\x0e\n\x06isNull\x18\x01 \x01(\x08\x12\x14\n\x0chostLanguage\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\x0c\"C\n\x0cRepeatedData\x12\x33\n\x08\x64\x61talist\x18\x01 \x03(\x0b\x32!.com.webank.ai.fate.api.core.Data\"r\n\x0b\x43\x61llRequest\x12\x0f\n\x07isAsync\x18\x01 \x01(\x08\x12\x0f\n\x07timeout\x18\x02 \x01(\x03\x12\x0f\n\x07\x63ommand\x18\x03 \x01(\t\x12\x30\n\x05param\x18\x04 \x01(\x0b\x32!.com.webank.ai.fate.api.core.Data\"\x82\x01\n\x0c\x43\x61llResponse\x12?\n\x0creturnStatus\x18\x01 \x01(\x0b\x32).com.webank.ai.fate.api.core.ReturnStatus\x12\x31\n\x06result\x18\x02 \x01(\x0b\x32!.com.webank.ai.fate.api.core.Data\"\"\n\x03Job\x12\r\n\x05jobId\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"V\n\x04Task\x12-\n\x03job\x18\x01 \x01(\x0b\x32 .com.webank.ai.fate.api.core.Job\x12\x0e\n\x06taskId\x18\x02 \x01(\x03\x12\x0f\n\x07tableId\x18\x03 \x01(\x03\"K\n\x06Result\x12/\n\x04task\x18\x01 \x01(\x0b\x32!.com.webank.ai.fate.api.core.Task\x12\x10\n\x08resultId\x18\x02 \x01(\x03\"-\n\x0cReturnStatus\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\tB\x0b\x42\tBasicMetab\x06proto3')
)




_ENDPOINT = _descriptor.Descriptor(
  name='Endpoint',
  full_name='com.webank.ai.fate.api.core.Endpoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ip', full_name='com.webank.ai.fate.api.core.Endpoint.ip', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='com.webank.ai.fate.api.core.Endpoint.port', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hostname', full_name='com.webank.ai.fate.api.core.Endpoint.hostname', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=48,
  serialized_end=102,
)


_ENDPOINTS = _descriptor.Descriptor(
  name='Endpoints',
  full_name='com.webank.ai.fate.api.core.Endpoints',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='endpoints', full_name='com.webank.ai.fate.api.core.Endpoints.endpoints', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=104,
  serialized_end=173,
)


_DATA = _descriptor.Descriptor(
  name='Data',
  full_name='com.webank.ai.fate.api.core.Data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='isNull', full_name='com.webank.ai.fate.api.core.Data.isNull', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hostLanguage', full_name='com.webank.ai.fate.api.core.Data.hostLanguage', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='com.webank.ai.fate.api.core.Data.type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='com.webank.ai.fate.api.core.Data.data', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=175,
  serialized_end=247,
)


_REPEATEDDATA = _descriptor.Descriptor(
  name='RepeatedData',
  full_name='com.webank.ai.fate.api.core.RepeatedData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='datalist', full_name='com.webank.ai.fate.api.core.RepeatedData.datalist', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=249,
  serialized_end=316,
)


_CALLREQUEST = _descriptor.Descriptor(
  name='CallRequest',
  full_name='com.webank.ai.fate.api.core.CallRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='isAsync', full_name='com.webank.ai.fate.api.core.CallRequest.isAsync', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeout', full_name='com.webank.ai.fate.api.core.CallRequest.timeout', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='command', full_name='com.webank.ai.fate.api.core.CallRequest.command', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='param', full_name='com.webank.ai.fate.api.core.CallRequest.param', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=318,
  serialized_end=432,
)


_CALLRESPONSE = _descriptor.Descriptor(
  name='CallResponse',
  full_name='com.webank.ai.fate.api.core.CallResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='returnStatus', full_name='com.webank.ai.fate.api.core.CallResponse.returnStatus', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='result', full_name='com.webank.ai.fate.api.core.CallResponse.result', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=435,
  serialized_end=565,
)


_JOB = _descriptor.Descriptor(
  name='Job',
  full_name='com.webank.ai.fate.api.core.Job',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='jobId', full_name='com.webank.ai.fate.api.core.Job.jobId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='com.webank.ai.fate.api.core.Job.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=567,
  serialized_end=601,
)


_TASK = _descriptor.Descriptor(
  name='Task',
  full_name='com.webank.ai.fate.api.core.Task',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='job', full_name='com.webank.ai.fate.api.core.Task.job', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='taskId', full_name='com.webank.ai.fate.api.core.Task.taskId', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tableId', full_name='com.webank.ai.fate.api.core.Task.tableId', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=603,
  serialized_end=689,
)


_RESULT = _descriptor.Descriptor(
  name='Result',
  full_name='com.webank.ai.fate.api.core.Result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='task', full_name='com.webank.ai.fate.api.core.Result.task', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resultId', full_name='com.webank.ai.fate.api.core.Result.resultId', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=691,
  serialized_end=766,
)


_RETURNSTATUS = _descriptor.Descriptor(
  name='ReturnStatus',
  full_name='com.webank.ai.fate.api.core.ReturnStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='com.webank.ai.fate.api.core.ReturnStatus.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='com.webank.ai.fate.api.core.ReturnStatus.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=768,
  serialized_end=813,
)

_ENDPOINTS.fields_by_name['endpoints'].message_type = _ENDPOINT
_REPEATEDDATA.fields_by_name['datalist'].message_type = _DATA
_CALLREQUEST.fields_by_name['param'].message_type = _DATA
_CALLRESPONSE.fields_by_name['returnStatus'].message_type = _RETURNSTATUS
_CALLRESPONSE.fields_by_name['result'].message_type = _DATA
_TASK.fields_by_name['job'].message_type = _JOB
_RESULT.fields_by_name['task'].message_type = _TASK
DESCRIPTOR.message_types_by_name['Endpoint'] = _ENDPOINT
DESCRIPTOR.message_types_by_name['Endpoints'] = _ENDPOINTS
DESCRIPTOR.message_types_by_name['Data'] = _DATA
DESCRIPTOR.message_types_by_name['RepeatedData'] = _REPEATEDDATA
DESCRIPTOR.message_types_by_name['CallRequest'] = _CALLREQUEST
DESCRIPTOR.message_types_by_name['CallResponse'] = _CALLRESPONSE
DESCRIPTOR.message_types_by_name['Job'] = _JOB
DESCRIPTOR.message_types_by_name['Task'] = _TASK
DESCRIPTOR.message_types_by_name['Result'] = _RESULT
DESCRIPTOR.message_types_by_name['ReturnStatus'] = _RETURNSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Endpoint = _reflection.GeneratedProtocolMessageType('Endpoint', (_message.Message,), dict(
  DESCRIPTOR = _ENDPOINT,
  __module__ = 'fate_meta_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.api.core.Endpoint)
  ))
_sym_db.RegisterMessage(Endpoint)

Endpoints = _reflection.GeneratedProtocolMessageType('Endpoints', (_message.Message,), dict(
  DESCRIPTOR = _ENDPOINTS,
  __module__ = 'fate_meta_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.api.core.Endpoints)
  ))
_sym_db.RegisterMessage(Endpoints)

Data = _reflection.GeneratedProtocolMessageType('Data', (_message.Message,), dict(
  DESCRIPTOR = _DATA,
  __module__ = 'fate_meta_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.api.core.Data)
  ))
_sym_db.RegisterMessage(Data)

RepeatedData = _reflection.GeneratedProtocolMessageType('RepeatedData', (_message.Message,), dict(
  DESCRIPTOR = _REPEATEDDATA,
  __module__ = 'fate_meta_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.api.core.RepeatedData)
  ))
_sym_db.RegisterMessage(RepeatedData)

CallRequest = _reflection.GeneratedProtocolMessageType('CallRequest', (_message.Message,), dict(
  DESCRIPTOR = _CALLREQUEST,
  __module__ = 'fate_meta_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.api.core.CallRequest)
  ))
_sym_db.RegisterMessage(CallRequest)

CallResponse = _reflection.GeneratedProtocolMessageType('CallResponse', (_message.Message,), dict(
  DESCRIPTOR = _CALLRESPONSE,
  __module__ = 'fate_meta_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.api.core.CallResponse)
  ))
_sym_db.RegisterMessage(CallResponse)

Job = _reflection.GeneratedProtocolMessageType('Job', (_message.Message,), dict(
  DESCRIPTOR = _JOB,
  __module__ = 'fate_meta_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.api.core.Job)
  ))
_sym_db.RegisterMessage(Job)

Task = _reflection.GeneratedProtocolMessageType('Task', (_message.Message,), dict(
  DESCRIPTOR = _TASK,
  __module__ = 'fate_meta_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.api.core.Task)
  ))
_sym_db.RegisterMessage(Task)

Result = _reflection.GeneratedProtocolMessageType('Result', (_message.Message,), dict(
  DESCRIPTOR = _RESULT,
  __module__ = 'fate_meta_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.api.core.Result)
  ))
_sym_db.RegisterMessage(Result)

ReturnStatus = _reflection.GeneratedProtocolMessageType('ReturnStatus', (_message.Message,), dict(
  DESCRIPTOR = _RETURNSTATUS,
  __module__ = 'fate_meta_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.api.core.ReturnStatus)
  ))
_sym_db.RegisterMessage(ReturnStatus)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
