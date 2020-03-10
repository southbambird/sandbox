strs = gets.chomp
search_str = gets.chomp

strs += strs

if strs.include? search_str
  puts "Yes"
else
  puts "No"
end
