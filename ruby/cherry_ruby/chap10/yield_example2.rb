def greeting
  puts 'hi'
  result = yield 'hello'
  puts result
  puts 'see you'
end


greeting do |text|
  text * 2
end
