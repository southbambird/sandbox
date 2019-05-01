def greeting &block
  puts 'good morning!'
  text = block.call('hello!')
  puts text
  puts 'good evening'
end

greeting do |text|
  text * 2
end
