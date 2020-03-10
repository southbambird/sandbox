alphabet = ('a'..'z')
table = Hash.new(0)
alphabet.each{|m| table[m] = 0}

while str = gets
  str.chomp!

  str.downcase.scan(/./)do |m|
    if alphabet.cover? m
      table[m] += 1
    end
  end
end

table.each do |key, num|
  printf "%s : %d\n", key , num
end
