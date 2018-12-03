greeter = Proc.new {|name|
  puts "Hello, #{name}"
}

greeter.call 'Proc'
greeter.call 'Ruby'

format = Proc.new do |name|
  name = name.capitalize

  "Hello, #{name}"
end

puts format.call 'alice'
