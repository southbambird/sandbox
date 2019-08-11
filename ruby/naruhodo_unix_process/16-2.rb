child_process = 3
dead_process  = 0

sleep_time = 3
child_process.times do
  fork do
    sleep sleep_time
  end
  sleep_time += 1
end

$stdout.sync = true

trap(:CHLD) do
  begin
    while pid = Process.wait(-1,Process::WNOHANG)
      puts pid
      dead_process += 1
    end
  rescue Errno::ECHILD
  end
end

loop do
  puts dead_process
  exit if dead_process == child_process

  sleep 1
end
