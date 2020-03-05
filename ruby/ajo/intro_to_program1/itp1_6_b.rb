def suit_to_int(suit)
  case suit
  when 'S'
    0
  when 'H'
    1
  when 'C'
    2
  when 'D'
    3
  end
end

CARD_NUM = 13
SUITS = ['S','H','C','D']
n = gets.chop.to_i

card = Array.new(SUITS.size).map{Array.new(CARD_NUM,0)}

1.step n do
  suit, num = gets.chop.split(' ')
  suit = suit_to_int(suit)
  num = num.to_i
  card[suit][num-1] = 1
end

SUITS.each do |suit|
  1.step CARD_NUM do |num|
    if card[suit_to_int(suit)][num-1] == 0
      printf "%s %d\n", suit, num
    end
  end
end
