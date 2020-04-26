this_dir = File.expand_path(__dir__)
lib_dir = File.join(this_dir, 'lib')
$LOAD_PATH.unshift(lib_dir) unless $LOAD_PATH.include?(lib_dir)

require 'eventify_services_pb'
require 'grpc'
require 'multi_json'
require 'pry'
require 'rb-readline'
require 'event_generator'

include Eventify

class EventEnumerator
  def initialize(generator, type)
    @subscribed_type = type
    @event_queue = Queue.new

    generator.add_observer(self)
  end

  def each
    return enum_for(:each) unless block_given?

    loop do
      yield @event_queue.pop
    end
  end

  def update(event)
    @event_queue.push(event) if event.type == @subscribed_type
  end
end

class EventifyImpl < Eventify::Eventify::Service
  def initialize(locations)
    @event_generator = EventGenerator.new(locations)
    Thread.new { @event_generator.run }
  end

  def subscribe(request, _call)
    puts("Got connection")

    EventEnumerator.new(@event_generator, request.type).each
  end
end

def main
  raise 'Specify path to locations file' if ARGV.empty?

  locations = []
  File.open(ARGV[0]) do |f|
    locations = MultiJson.load(f.read)
  end

  port = '0.0.0.0:50051'
  s = GRPC::RpcServer.new
  s.add_http2_port(port, :this_port_is_insecure)
  GRPC.logger.info("... running insecurely on #{port}")
  s.handle(EventifyImpl.new(locations))
  s.run_till_terminated_or_interrupted([1, 'int', 'SIGQUIT'])
end

main
