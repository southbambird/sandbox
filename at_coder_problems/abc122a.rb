def get_pair_base(base)
  pair = {"A" => "T", "T" => "A", "C" => "G", "G" => "C"}
  return pair[base]
end

puts get_pair_base(gets.chomp)
