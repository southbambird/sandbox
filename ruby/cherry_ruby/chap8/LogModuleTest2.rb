module Loggable
  def log(text)
    p "[LOG] #{text}"
  end
end

class Product
  extend Loggable

  def self.create_products(name)
    log 'create_products is called.'
  end
end

Product.create_products([])

Product.log('Hello.')
