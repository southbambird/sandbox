def count_acgt(string)
  string.gsub!(/[^ACGT]/,',')
  list = string.split(',')
  result = 0
  list.each do |item|
    result = item.size if item.size > result
  end
  result
end

puts count_acgt(gets.chomp)
