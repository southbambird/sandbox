r, c = gets.chop.split(' ').map(&:to_i)

table = Array.new(r+1).map{Array.new(c+1,0)}

r.times do |i|
  row = gets.chop.split(' ').map(&:to_i)
  c.times do |j|
    table[i][j] = row[j]
    table[r][j] += row[j]
    table[i][c] += row[j]
    table[r][c] += row[j]
  end
end


table.each do |row|
  row.each_with_index do |column,cindex|
    print column
    print ' ' if cindex != c
  end
  puts ''
end
