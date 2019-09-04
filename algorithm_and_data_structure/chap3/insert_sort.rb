N = gets.to_i
A = gets.chop.split.map(&:to_i)

p A

def insert_sort(a, n)
  1.upto N-1 do |i|
    v = a[i]
    j = i - 1
    while j >= 0 and a[j] > v
      a[j+1] = a[j]
      j = j - 1
    end
    a[j+1] = v
    p a
  end
end


insert_sort(A, N)
