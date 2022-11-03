"""Week 7 exercises"""


class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __repr__(self):
        return f"City(name = {self.name}, population = {self.population})"

    def __add__(self, other: "City"):
        return City(self.name, self.population + other.population)


def test_city():
    home = City("Home", 5000)
    away = City("Away", 10399)
    print(home)
    print(away)
    print(home + away)


if __name__ == '__main__':
    test_city()
