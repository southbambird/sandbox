loop do
  card = gets.chop
  if card == "-"
    break
  end
  num = gets.chop.to_i

  shuffle_num = 0
  num.times do
    shuffle_num += gets.chop.to_i
  end

  shuffle_num = shuffle_num % card.size

  puts card.slice(shuffle_num..(card.size)) + card.slice(0,shuffle_num)
end
