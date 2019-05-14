def buy_tickets(*name_list)
  if name_list.size <= 3
    name_list.each do |name|
      puts "Buying a ticket for #{name}"
    end
  else
    puts "Buying a group ticket for #{name_list.join(", ")}."
  end
end


buy_tickets("Sam", "Dave", "David")
buy_tickets("John", "Paul", "Ringo", "George")
