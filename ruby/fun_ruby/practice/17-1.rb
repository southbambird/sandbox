def count_line(file_path)
  File.open(file_path) do |file|
    count = 0
    file.each_line {count += 1}
    return count
  end
end
    
p count_line("./test.txt")
