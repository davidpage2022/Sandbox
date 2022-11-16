"""Week 9 exercises"""

import datetime

DAYS_PER_YEAR = 365.2425


class Person:
    def __init__(self, name: str, date_of_birth: datetime.date):
        self.name = name
        self.date_of_birth = date_of_birth

    def __str__(self):
        date_string = datetime.datetime.strftime(self.date_of_birth, "%d/%m/%Y")
        return f"{self.name} ({date_string})"

    def __repr__(self):
        return str(vars(self))

    @property
    def age(self) -> int:
        return int((datetime.date.today() - self.date_of_birth).days / DAYS_PER_YEAR)


class Student(Person):
    def __init__(self, student_id, course, **kwargs):
        # Person.__init__(self, name, date_of_birth)
        # super(Student, self).__init__(name, date_of_birth)
        super().__init__(**kwargs)
        self.course = course
        self.id = student_id

    def __repr__(self):
        return str(vars(self))

    def __str__(self):
        return f"{super().__str__()}, student ID: {self.id}, course: {self.course}"


class Employee(Person):
    def __init__(self, salary, **kwargs):
        super().__init__(**kwargs)
        self.salary = salary

    def __repr__(self):
        return str(vars(self))

    def __str__(self):
        return f"{super().__str__()} ${self.salary:.2f}"


class Musician(Person):
    def __init__(self, style, **kwargs):
        super().__init__(**kwargs)
        self.style = style

    def __repr__(self):
        return str(vars(self))

    def play(self, duration):
        print(f"Playing for {duration} seconds in {self.style} style...")


def test_person():
    person = Person("John Smith", datetime.date(1992, 1, 1))
    print(person.name)
    print(person.age)


def test_student():
    student = Student(name="Jane Doe", date_of_birth=datetime.date(1992, 1, 1),
                      student_id=3523676, course="Information Technology")
    print(student)
    print(student.age)


def test_employee():
    employee = Employee(name="Bob", date_of_birth=datetime.date(1892, 1, 1),
                        salary=500)
    print(employee)
    print(employee.salary)


def test_musician():
    musician = Musician(name="Sally", date_of_birth=datetime.date(1900, 2, 15),
                        style="blues")
    print(musician)
    print(musician.style)
    musician.play(5)


if __name__ == '__main__':
    # test_person()
    test_student()
    test_employee()
    # test_musician()