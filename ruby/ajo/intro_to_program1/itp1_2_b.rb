a, b, c = gets.chop.split(' ')

a = a.to_i
b = b.to_i
c = c.to_i

if a < b && b < c
  puts "Yes"
else
  puts "No"
end
