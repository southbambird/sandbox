def search(array, n, key)
  i = 0
  array[n] = key
  while array[i] != key
    i += 1
  end
  return i != n
end



n = gets.chop.to_i
s_ary = gets.chop.split.map(&:to_i)
q = gets.chop.to_i
t_ary = gets.chop.split.map(&:to_i)

sum = 0
q.times do |i|
  sum += 1 if search(s_ary, n, t_ary[i])
end


puts sum

