a = (1..100).to_a

result = 0
a.each {|n| result += n}
p result

p a.inject{|result, n| result += n}
