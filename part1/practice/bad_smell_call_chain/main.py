# Измените класс Person так, чтобы его методы 
# оперировали внутренним состоянием, 
# а не использовали цепочку вызовов объектов

class Location:
    def room(self):
        return 42

    def population(self):
        return 100500


class Person:
    def __init__(self):
        self.location = Location()

    def get_person_room(self):
        return self.location.room()

    def get_city_population(self):
        return self.location.population()


b = Person()
print(b.get_person_room())
print(b.get_city_population())
