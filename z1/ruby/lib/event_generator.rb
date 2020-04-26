require 'observer'
require 'eventify_services_pb'
require 'date'

include Eventify

# Generates new events in random intervals
class EventGenerator
  include Observable

  def initialize(locations)
    @locations = locations
    @event_counter = 0
  end

  def run
    loop do
      sleep_random

      new_event = generate_event
      puts("Generated new event: #{new_event}")
      changed
      notify_observers(new_event)
    end
  end

  private

  def sleep_random
    interval = rand(1...5)
    sleep interval
  end

  def generate_event
    Event.new(
      name: new_event_name,
      type: new_event_type,
      instances: new_event_instances
    )
  end

  def new_event_name
    name = "Event #{@event_counter}"
    @event_counter += 1
    name
  end

  def new_event_type
    type_name = "EventType::#{EventType.constants.sample}"
    Object.const_get(type_name)
  end

  def new_event_instances
    instances = []
    rand(1..3).times do
      instances.append(
        Event::Instance.new(
          location: new_event_instance_location,
          date: new_event_instance_date
        )
      )
    end
    instances
  end

  def new_event_instance_location
    @locations.sample
  end

  def new_event_instance_date
    (Date.today + rand(10...30)).to_s
  end
end
