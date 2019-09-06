def swap(a, j)
  temp = a[j]
  a[j] = a[j-1]
  a[j-1] = temp
end

def bubble_sort(a, n)
  (0..n).each do |i|
    (n-1).step(i+1, -1) do |j|
      if a[j] < a[j-1]
        swap(a, j)
      end
    end
    p a
  end
end

N = gets.to_i
A = gets.chop.split.map(&:to_i)

bubble_sort(A, N)
