# coding: utf-8
foo = 'foo in toplevel'

def display_foo
  # メソッドの外で定義されたローカル変数は使用できない
  puts foo
end

puts foo
# display_foo




greeting = "Hello, "
people   = ['Alice', 'Bob']

people.each do |person|
  # ブロックの外で定義された変数は使用できる
  puts greeting + person
end

# ブロックの中で定義された変数は使用できない
# puts person




$undefined




FOO_BAR = 'bar'
# 定義済み定数への再代入は禁止されていないが、実行時に警告が出る
FOO_BAR = 'foo'

puts FOO_BAR

def set_foo
  # メソッドの中で定数は定義できない
  # FOO_BAR = 'bar'
end
