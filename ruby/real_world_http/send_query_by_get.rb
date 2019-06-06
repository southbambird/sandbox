require "uri"
require "net/http"
require "logger"

logger = Logger.new(STDOUT)

params = Hash.new
params.store("query1","hello, world")
params.store("query2","hello, new world")
url = URI.parse("http://localhost:18888?#{URI.encode_www_form(params)}")

begin
  res = Net::HTTP.start(url.host, url.port) do |http|
    http.get('/')
  end
  logger.info res.body

rescue
  logger.error "connection failed."
end
