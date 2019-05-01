def greeting &block
  puts 'good morning!'
  unless block.nil?
    text = block.call('hello!')
    puts text
  end
  puts 'good evening'
end

greeting do |text|
  text * 2
end

greeting
