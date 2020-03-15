search_text = gets.chop

count = 0

loop do
  text = gets.chop.downcase
  if text == "END_OF_TEXT".downcase
    break
  end
  count = count + text.scan(search_text).size
end

puts count
