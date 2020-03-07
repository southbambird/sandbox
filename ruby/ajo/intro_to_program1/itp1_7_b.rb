loop do
  n, x = gets.chop.split(' ').map(&:to_i)
  if n == 0 && x == 0
    break
  end

  count = 0
  
  1.step n do |a|
    (a+1).step n do |b|
      (b+1).step n do |c|
        count += 1 if a+b+c == x
      end
    end
  end
  puts count
end
