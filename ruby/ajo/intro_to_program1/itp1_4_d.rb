n = gets.chop.to_i
list = gets.chop.split(' ').map(&:to_i)

max = -1000000
min = 1000000
total = 0

list.each do |n|
  total = total + n
  max = n if max < n
  min = n if min > n
end

printf "%d %d %d\n", min, max, total
