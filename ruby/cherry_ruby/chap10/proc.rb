def greeting(&proc)
  puts 'good morning'
  text = proc.call('hello!')
  puts text
  puts 'good evening'
end

repeat_proc = Proc.new {|text| text * 2}
greeting(&repeat_proc)
