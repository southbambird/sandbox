# coding: utf-8
def clever_print(*args)
  args.each do |item|
    case item
    when Array
      item.each do |value|
        print value, " "
      end
    when Hash
      item.each do |key, value|
        print key, " ", value, " "
      end
    when String
      print item, " "
    end
  end
  print "\n"
end


=begin
def clever_print_kai(*args)
  list = []
  args.each {|item| list << item.to_a}
  # Ruby1.9 で String クラスから to_aメソッドは廃止された
  puts list.join(' ')
end
=end

clever_print(["Ruby"], "the", ["Programming", "Language"])
#=> Ruby the Programming Language
 
clever_print(["Agile", "Web", "Development"], "with", { :Rails => 3.0 })
#=> Agile Web Development with Rails 3.0
