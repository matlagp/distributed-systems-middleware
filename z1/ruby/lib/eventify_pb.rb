# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: eventify.proto

require 'google/protobuf'

Google::Protobuf::DescriptorPool.generated_pool.build do
  add_file("eventify.proto", :syntax => :proto3) do
    add_message "eventify.SubRequest" do
      optional :type, :enum, 1, "eventify.EventType"
    end
    add_message "eventify.Event" do
      optional :name, :string, 1
      optional :type, :enum, 2, "eventify.EventType"
      repeated :instances, :message, 3, "eventify.Event.Instance"
    end
    add_message "eventify.Event.Instance" do
      optional :location, :string, 1
      optional :date, :string, 2
    end
    add_enum "eventify.EventType" do
      value :CONCERT, 0
      value :CONFERENCE, 1
      value :FESTIVAL, 2
    end
  end
end

module Eventify
  SubRequest = ::Google::Protobuf::DescriptorPool.generated_pool.lookup("eventify.SubRequest").msgclass
  Event = ::Google::Protobuf::DescriptorPool.generated_pool.lookup("eventify.Event").msgclass
  Event::Instance = ::Google::Protobuf::DescriptorPool.generated_pool.lookup("eventify.Event.Instance").msgclass
  EventType = ::Google::Protobuf::DescriptorPool.generated_pool.lookup("eventify.EventType").enummodule
end
