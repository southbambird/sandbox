def greeting
  p 'hi'
  yield
  p "how are you?"
end


greeting do
  p 'nice to meet you.'
end
