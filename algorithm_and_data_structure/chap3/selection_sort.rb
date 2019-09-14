N = gets.to_i
A = gets.chop.split.map(&:to_i)

def selection_sort(a, n)
  (n-1).times do |i|
    minj = i
    (i..n-1).each do |j|
      minj = j if a[j] < a[minj]
    end
    temp = a[i]
    a[i] = a[minj]
    a[minj] = temp

    p a
  end
end

selection_sort(A, N)
