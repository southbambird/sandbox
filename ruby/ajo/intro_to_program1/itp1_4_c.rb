1.step do
  input_list = gets.chop.split(' ')
  a = input_list.fetch(0).to_i
  b = input_list.fetch(2).to_i
  op = input_list.fetch(1)

  case op
  when '+'
    puts a + b
  when '-'
    puts a - b
  when '*'
    puts a * b
  when '/'
    puts a / b
  when '?'
    break
  end
end
