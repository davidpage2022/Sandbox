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


class Student(Person):
    def __init__(self, name, date_of_birth, student_id, course):
        # Person.__init__(self, name, date_of_birth)
        # super(Student, self).__init__(name, date_of_birth)
        super().__init__(name, date_of_birth)
        self.course = course
        self.id = student_id

    def __repr__(self):
        return str(vars(self))


def test_person():
    person = Person("John Smith", datetime.date(1992, 1, 1))
    print(person.name)
    print(person.age)


def test_student():
    student = Student("Jane Doe", datetime.date(1992, 1, 1), 3523676, "Information Technology")
    print(student)
    print(student.age)


if __name__ == '__main__':
    # test_person()
    test_student()
