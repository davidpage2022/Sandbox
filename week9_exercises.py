"""Week 9 exercises"""

import datetime

DAYS_PER_YEAR = 365.2425


class Person:
    def __init__(self, name: str, date_of_birth: datetime.date):
        self.name = name
        self.date_of_birth = date_of_birth

    def __repr__(self):
        date_string = datetime.datetime.strftime(self.date_of_birth, "%d/%m/%Y")
        return f"{self.name} ({date_string})"

    @property
    def age(self) -> int:
        return int((datetime.date.today() - self.date_of_birth).days / DAYS_PER_YEAR)


def test_person():
    person = Person("John Smith", datetime.date(1992, 1, 1))
    print(person.name)
    print(person.age)


if __name__ == '__main__':
    test_person()
