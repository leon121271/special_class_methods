from module_5.attributes_and_methods import House
class AdvancedHouse(House):
    def get_number_of_floors(self):
        return self.number_of_floors


h1 = AdvancedHouse('ЖК Эльбрус', 10)
h2 = AdvancedHouse('ЖК Акация', 20)

print(h1)
print(h2)
print(h1.get_number_of_floors())
print(h2.get_number_of_floors())