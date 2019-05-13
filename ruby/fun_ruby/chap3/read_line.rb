filename = ARGV[0]
file = File.open(filename)
file.each_line do |text|
  print text
end
file.close
