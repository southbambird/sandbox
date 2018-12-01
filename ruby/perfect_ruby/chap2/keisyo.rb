class Parent
  def hello
    puts 'Hello, Parent class!'
  end
end


class Chile < Parent
  def hi
    puts 'Hello, Child class!'
  end
end


child = Chile.new
child.hello
child.hi


class Child < Parent
  def hello
    super

    puts 'Hello, Chiled class!'
  end
end

child = Child.new
child.hello
