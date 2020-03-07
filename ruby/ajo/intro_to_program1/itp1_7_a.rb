info = Array.new
0.step do 
  m, f, r = gets.chop.split(' ').map(&:to_i)
  if m == -1 && f == -1 && r == -1
    break
  end
  info.append([m, f, r])
end

info.each do |m, f, r|
  if m == -1 or f == -1
    puts "F"
  elsif m + f >= 80
    puts "A"
  elsif m + f >= 65 && m + f < 80
    puts "B"
  elsif m + f >= 50 && m + f < 65
    puts "C"
  elsif m + f >= 30 && m + f < 50
    if r >= 50
      puts "C"
    else
      puts "D"
    end
  elsif m + f < 30
    puts "F"
  else
    puts "error!"
  end
end
