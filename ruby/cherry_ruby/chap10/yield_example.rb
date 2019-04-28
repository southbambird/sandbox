def greeting
  p 'hi'
  if block_given?
    yield
  end
  p "how are you?"
end

greeting

greeting do
  p 'nice to meet you.'
end
