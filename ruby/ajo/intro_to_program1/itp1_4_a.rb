a, b = gets.chop.split(' ').map(&:to_i)
printf "%s %s %.5f\n", a / b, a % b, a.to_f / b.to_f
