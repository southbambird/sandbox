# coding: utf-8
foo = 'foo in toplevel'

def display_foo
  # メソッドの外で定義されたローカル変数は使用できない
  puts foo
end


puts foo
display_foo
