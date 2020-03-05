n, m = gets.chop.split(' ').map(&:to_i)
a = Array.new(n).map{Array.new(m,0)}
0.step n-1 do |i|
  a[i] = gets.chop.split(' ').map(&:to_i)
end
b = Array.new(m,0)
0.step m-1 do |j|
  b[j] = gets.chop.to_i
end

0.step n-1 do |ni|
  tmp = 0
  0.step m-1 do |mj|
    tmp += a[ni][mj] * b[mj]
  end
  puts tmp
end
