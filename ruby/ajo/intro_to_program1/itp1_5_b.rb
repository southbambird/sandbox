1.step do
  h, w = gets.chop.split(' ').map(&:to_i)
  break if h == 0 && w == 0

  1.step h do |hi|
    1.step w do |wi|
      if hi == 1 or wi == 1 or hi == h or wi == w
        putc '#'
      else
        putc '.'
      end
    end
    puts ''
  end
  puts ''
end
