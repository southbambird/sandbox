N = gets.to_i
A = gets.chop.split.map(&:to_i)

p A

def bubble_sort(a, n)
  flag = true
  i = 0
  while flag
    flag = false
    (n-1).step( i+1, -1) do |j|
      if a[j] < a[j-1]
        temp = a[j]
        a[j] = a[j-1]
        a[j-1] = temp
        flag = true
      end
    end
    i = i + 1
    p a
  end
end

bubble_sort(A, N)
