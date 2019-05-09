a = (1..100).to_a

a3 = a.reject{|n| n % 3 != 0}
p a3

a.reject!{|n| n % 3 != 0}
p a
