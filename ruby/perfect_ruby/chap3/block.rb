def display_value
  puts yield
end

display_value do
  4423
end

display_value do
  next 42
end

display_value do
  break 42
end
