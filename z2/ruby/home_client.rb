require_relative 'home'

class HomePrx
  def initialize(communicator)
    @communicator = communicator
  end

  def evaluate(args)
    subsystem = args.shift
    operation = args.shift

    begin
      prx = resolve_subsystem(subsystem)
      if args.empty?
        handle_response prx.send(operation.to_sym)
      else
        handle_response prx.send(operation.to_sym, args.first.to_i)
      end
    rescue Home::AlreadyOnException, Home::AlreadyOffException => _e
      puts 'Device state unchanged'
    rescue Home::InvalidOperationException => _e
      puts 'Make sure the device is on!'
    rescue NoMethodError => _e
      puts 'Wrong method'
    rescue Ice::UnknownException => _e
      puts 'Something went wrong...'
    end
  end

  private

  def resolve_subsystem(subsystem_name)
    case subsystem_name.downcase
    when 'cctv'
      cctv_prx
    when 'lightsensor'
      light_sensor_prx
    when 'soundsensor'
      sound_sensor_prx
    end
  end

  def cctv_prx
    @cctv_prx ||= begin
      base = @communicator.stringToProxy("home/cctv:tcp -h localhost -p 10000")
      Home::CCTVPrx::checkedCast(base)
    end
  end

  def light_sensor_prx
    @light_sensor_prx ||= begin
      base = @communicator.stringToProxy("home/lightsensor:tcp -h localhost -p 10000")
      Home::LightSensorPrx::checkedCast(base)
    end
  end

  def sound_sensor_prx
    @sound_sensor_prx ||= begin
      base = @communicator.stringToProxy("home/soundsensor:tcp -h localhost -p 10000")
      Home::SoundSensorPrx::checkedCast(base)
    end
  end

  def handle_response(response)
    if response.class == Home::CCTVStatus
      puts "Zoom: #{response.zoom}"
      puts "Tilt: #{response.theta}"
    elsif response.respond_to?(:to_s)
      puts response
    end
  end
end

Ice::initialize(ARGV) do |communicator|
  home_prx = HomePrx.new(communicator)
  loop do
    line = STDIN.gets.chomp
    home_prx.evaluate(line.split(' '))
  end
end
