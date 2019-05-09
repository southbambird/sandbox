a = (1..100).to_a

a2 = a.collect {|n| n * 100}
p a2

a.collect!{|n| n * 100}
p a
