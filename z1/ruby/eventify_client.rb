this_dir = File.expand_path(__dir__)
lib_dir = File.join(this_dir, 'lib')
$LOAD_PATH.unshift(lib_dir) unless $LOAD_PATH.include?(lib_dir)

require 'eventify_services_pb'
require 'grpc'

include Eventify

def subscribe_for_type(stub, type_name)
  subscription_string = "Subscribed: #{type_name}"
  puts(subscription_string)
  puts('-' * subscription_string.length)

  request = SubRequest.new(
    type: string_to_event_type(type_name)
  )

  events = stub.subscribe(request)
  events.each do |event|
    puts("New #{type_name} event: #{event}")
  end
end

def string_to_event_type(name)
  case name.upcase
  when 'CONCERT'
    EventType::CONCERT
  when 'CONFERENCE'
    EventType::CONFERENCE
  when 'FESTIVAL'
    EventType::FESTIVAL
  else
    raise ArgumentError, "Unrecognized event type: #{name}"
  end
end

def main
  stub = Eventify::Eventify::Stub.new('localhost:50051', :this_channel_is_insecure)

  if ARGV.empty?
    puts('Supply at least one event type')
    exit
  end

  ARGV.each do |event_type|
    begin
      Thread.new do
        subscribe_for_type(stub, event_type)
      end
    rescue ArgumentError => e
      puts(e)
    end
  end

  loop do
    STDIN.gets
  end
end

begin
  main
rescue Interrupt => _e
  exit
end
