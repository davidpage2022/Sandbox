"""Week 7 exercises"""


class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __repr__(self):
        return f"City(name = {self.name}, population = {self.population})"

    def __add__(self, other: "City"):
        return City(self.name, self.population + other.population)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age


def test_city():
    home = City("Home", 5000)
    away = City("Away", 10399)
    print(home)
    print(away)
    print(home + away)


def test_person():
    people = [Person("Bob", 35), Person("Jane", 29), Person("Bill", 29), Person("Bob", 35)]
    print(people[0] == people[1])
    print(people[1] == people[2])
    print(people[3] == people[0])


if __name__ == '__main__':
    test_person()
