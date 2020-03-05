1.step do
  h, w = gets.chop.split(' ').map(&:to_i)

  break if h == 0 && w == 0
  
  1.step h do
    1.step w do
      putc '#'
    end
    puts ''
  end
  puts ''
end
