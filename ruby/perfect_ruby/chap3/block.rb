def display_value
  puts yield
end

display_value do
  4423
end

display_value do
  next 42
end

display_value do
  break 42
end



def with_current_time
  yield Time.now
end

with_current_time do |now|
  puts now.year
end


def block_sample(&block)
  puts 'stand up'

  block.call if block

  puts 'sit down'
end

block_sample do
  puts 'walk'
end


people = %w(Alice Bob Charlie)
block = Proc.new do |name| puts name end
people.each &block
                 
p1 = Proc.new {|val| val.upcase }
p2 = :upcase.to_proc

p1.call 'hi'
p2.call 'hi'

people = %w(Alice Bob Carol)

people.map {|person| person.upcase }
people.map &:upcase





