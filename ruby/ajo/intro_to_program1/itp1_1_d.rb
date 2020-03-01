n = gets.chop.to_i

h = n / 3600
n1 = n % 3600

m = n1 / 60
s = n1 % 60

printf("%d:%d:%d\n", h, m, s)
