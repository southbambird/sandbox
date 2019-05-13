class Planet
  def life?
    puts "Who knows?"
  end
end

pluto = Planet.new()
earth = Planet.new()
mars  = Planet.new()

class << pluto
  def life?
    puts "Probably not."
  end
end

class << earth
  def life?
    puts "Positively!"
  end
end

pluto.life?
earth.life?
mars.life?
