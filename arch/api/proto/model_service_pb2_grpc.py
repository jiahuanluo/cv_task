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
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import model_service_pb2 as model__service__pb2


class ModelServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.publishLoad = channel.unary_unary(
        '/com.webank.ai.fate.api.mlmodel.manager.ModelService/publishLoad',
        request_serializer=model__service__pb2.PublishRequest.SerializeToString,
        response_deserializer=model__service__pb2.PublishResponse.FromString,
        )
    self.publishBind = channel.unary_unary(
        '/com.webank.ai.fate.api.mlmodel.manager.ModelService/publishBind',
        request_serializer=model__service__pb2.PublishRequest.SerializeToString,
        response_deserializer=model__service__pb2.PublishResponse.FromString,
        )


class ModelServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def publishLoad(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def publishBind(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ModelServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'publishLoad': grpc.unary_unary_rpc_method_handler(
          servicer.publishLoad,
          request_deserializer=model__service__pb2.PublishRequest.FromString,
          response_serializer=model__service__pb2.PublishResponse.SerializeToString,
      ),
      'publishBind': grpc.unary_unary_rpc_method_handler(
          servicer.publishBind,
          request_deserializer=model__service__pb2.PublishRequest.FromString,
          response_serializer=model__service__pb2.PublishResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'com.webank.ai.fate.api.mlmodel.manager.ModelService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
