_ = gets.chop.to_i
list = gets.chop.split(' ').map(&:to_i)

list.reverse.each_with_index do |n, i|
  print ' ' if i != 0
  print n
end
puts ''
