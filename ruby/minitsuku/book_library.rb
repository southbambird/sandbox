class Book
  def initialize(args)
    args[:library] << {author: args[:author], title: args[:title]}
  end
end

class Library
  def initialize
    @library = []
  end

  def to_s
    puts "Library contents:"
    @library.each do |book|
      puts "Title: #{book[:title]}, Author: #{book[:author]}"
    end
  end

  def <<(item)
    @library << item
  end
end

my_library = Library.new
Book.new(:author => "Herman Melville", :title => "Moby-Dick", :library => my_library)
Book.new(:author => "Hans Christian Andersen", :title => "The Ugly Duckling", :library => my_library)
puts my_library
