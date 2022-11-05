class A:
    def __init__(self, x):
        self.x = x

    def __str__(self):
        return f"{self.x}"

    # def __add__(self, other):
    #     return self.x + other.x

    def __sub__(self, other):
        return self.x - other.x


a = A(5)
b = A(10)

print(a - b)
