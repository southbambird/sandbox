class Ruler
  def length=(val)
    @length = val
  end

  def length
    @length
  end
end

ruler = Ruler.new

ruler.length = 30
puts ruler.length


class Ruler
  attr_accessor :length
end


class Ruler
  attr_accessor :length

  def set_default_length
    self.length = 30
  end
end

ruler = Ruler.new
ruler.set_default_length

puts ruler.length


class Ruler
  attr_accessor :length

  def initialize(length)
    @length = length
  end
end

ruler = Ruler.new(30)
puts ruler.length
