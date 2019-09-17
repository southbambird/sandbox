def binarySearch(array, n, key)
  left  = 0
  right = n
  while left < right
    mid = ((left + right) / 2).floor
    return true if key == array[mid]

    if key > array[mid]
      left = mid + 1
    else
      right = mid
    end
  end
end


n = gets.chop.to_i
s_ary = gets.chop.split.map(&:to_i)
q = gets.chop.to_i
t_ary = gets.chop.split.map(&:to_i)

sum = 0
q.times do |i|
  sum += 1 if binarySearch(s_ary, n, t_ary[i])
end


puts sum
