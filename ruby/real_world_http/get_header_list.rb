require 'net/http'
require 'logger'
require 'uri'

logger = Logger.new(STDOUT)

url = URI.parse('http://localhost:18888')

begin
  res = Net::HTTP.start(url.host, url.port) do |http|
    http.head('/')
  end

  res.each do |key, value|
    logger.info key + ":" + value
  end

rescue
  logger.error "connection failed."
end
