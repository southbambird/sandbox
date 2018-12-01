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


class Ruler
  attr_accessor :length

  def self.pair
    [Ruler.new(30), Ruler.new(30)]
  end
end


puts Ruler.pair


class MyClass
  @@cvar = 'Hello, My class variable!'

  def cvar_in_method
    puts @@cvar
  end

  def self.cvar_in_method
    puts @@cvar
  end
end

my_object = MyClass.new

my_object.cvar_in_method
MyClass.cvar_in_method
