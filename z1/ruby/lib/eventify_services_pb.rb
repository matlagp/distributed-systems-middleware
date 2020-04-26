# Generated by the protocol buffer compiler.  DO NOT EDIT!
# Source: eventify.proto for package 'eventify'

require 'grpc'
require 'eventify_pb'

module Eventify
  module Eventify
    # Sort of like event notify, but shorter
    class Service

      include GRPC::GenericService

      self.marshal_class_method = :encode
      self.unmarshal_class_method = :decode
      self.service_name = 'eventify.Eventify'

      # Subscribe for a particular event type
      rpc :Subscribe, SubRequest, stream(Event)
    end

    Stub = Service.rpc_stub_class
  end
end
