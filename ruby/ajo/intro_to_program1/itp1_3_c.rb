1.step 3000 do |i|
  a, b = gets.chop.split(' ').map(&:to_i)
  
  if a == 0 && b == 0
    break
  elsif a < b
    printf "%d %d\n", a, b
  else
    printf "%d %d\n", b, a
  end
end
