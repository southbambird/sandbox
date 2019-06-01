require "net/http"
require "logger"
require "uri"

logger = Logger.new(STDOUT)

url = URI.parse('http://localhost:18888')

begin
  res = Net::HTTP.start(url.host, url.port) do |http|
    http.get('/')
  end
  logger.info res.code + " " + res.message

rescue
  logger.error "connection failed."
end
