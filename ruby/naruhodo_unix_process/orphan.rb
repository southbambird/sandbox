fork do
  p Process.pid
  5.times do
    sleep 1
    puts "I'm an olphan!"
  end
end

p Process.pid
p Process.wait
abort "Parent process died...."
