def greeting(&block)
  puts 'good morning'
  text =
    if block.arity == 1
      yield 'hello'
    elsif block.arity == 2
      yield 'hel', 'lo'
    end
  puts text
  puts 'good evening'
end

greeting do |text|
  text * 2
end

greeting do |text_1, text_2|
  text_1 * 2 + text_2 * 2
end
