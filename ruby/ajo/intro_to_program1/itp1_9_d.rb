str = gets.chop
method_num = gets.chop.to_i

method_num.times do
  command_line = gets.chop.split(' ')
  method = command_line[0]
  case method
  when "print"
    a, b = command_line[1,2]
    puts str[a.to_i-1...b.to_i]
  when "reverse"
    a, b = command_line[1,2]
    str[a.to_i-1...b.to_i] = str[a.to_i-1...b.to_i].reverse
    puts "Reverse:" + str[a.to_i-1...b.to_i].reverse
    puts "Reverse:" + str
  when "replace"
    a, b, p = command_line[1,3]
    str[a.to_i-1...b.to_i] = p
    puts "Replace:" + str
  end
end

puts str
