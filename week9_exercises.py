"""Week 9 exercises"""

import datetime


class Person:
    def __init__(self, name: str, date_of_birth: datetime.date):
        self.name = name
        self.date_of_birth = date_of_birth

    def get_age(self) -> float:
        return datetime.date.today().year - self.date_of_birth.year


def test_person():
    person = Person("John Smith", datetime.date(1992, 1, 1))
    print(person.get_age())


if __name__ == '__main__':
    test_person()