battle_num = gets.chop.to_i
t_score = 0
h_score = 0
battle_num.times do
  t_card, h_card = gets.chop.split(' ')
  if t_card > h_card
    t_score += 3
  elsif t_card < h_card
    h_score += 3
  else
    t_score += 1
    h_score += 1
  end
end
printf("%d %d\n",t_score, h_score)
