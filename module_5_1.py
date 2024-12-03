class House:
    def __init__(self, name, number_of_floors): #Название, кол-во этажей.
        self.name = name
        self.number_of_floors = number_of_floors






h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
# h1.go_to(5)
# h2.go_to(10)

print(h1.name, h1.number_of_floors )
print(h2.name, h2.number_of_floors )