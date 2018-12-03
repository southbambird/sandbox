# coding: utf-8
# ブロックを使わずにファイルに書き込む
file = File.open('without_block.txt', 'w')
file.puts 'without block'
file.close

# ブロックを使ってファイルに書き込む
File.open('with_block.txt', 'w') do |file|
  file.puts 'with block'
end
