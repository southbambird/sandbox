class Queue
  attr_accessor :head ,:tail ,:queue
  MAX = 100000

  def initialize()
    @queue = []
    @head  = 0
    @tail  = 0
  end

  def isEmpty?()
    return @head == @tail
  end

  def isFull?()
    return @head == (@tail + 1) % MAX
  end

  def enqueue(x)
    if isFull?
      puts "queue is full!"
      return -1
    end

    @queue[@tail] = x
    (@tail+1) == MAX ? @tail = 0 : @tail += 1
  end

  def dequeue()
    if isEmpty?
      puts "queue is empty!"
      return -1
    end
    x = @queue[@head]
    @queue[@head] = nil
    (@head+1) == MAX ? @head = 0 : @head += 1

    return x
  end
end

MyProcess = Struct.new(:name, :time)
n, q = gets.chop.split.map(&:to_i)
queue = Queue.new
elaps = 0

n.times do |i|
  name, time = gets.chop.split
  queue.enqueue(MyProcess.new(name, time.to_i))
end

while (queue.head != queue.tail)
  u = queue.dequeue()
  c = [q, u.time].min
  u.time -= c
  elaps += c
  if u.time > 0
    queue.enqueue(u)
  else
    puts "#{u.name} #{elaps}"
  end
end
  
