1.step do
  h, w = gets.chop.split(' ').map(&:to_i)
  break if h == 0 && w == 0

  1.step h do |hi|
    1.step w do |wi|
      if (hi + wi) % 2 == 0
        putc '#'
      else
        putc '.'
      end
    end
    puts ''
  end
  puts ''
end
