require 'net/http'
require 'uri'

url = URI.parse('http://localhost:18888')

begin
  res = Net::HTTP.start(url.host, url.port) do |http|
    http.get('/')
  end

  puts res.body
  
rescue
  $stderr.puts "connection failed."
end

