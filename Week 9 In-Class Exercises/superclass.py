class SuperClass:
    def __init__(self, x):
        self.x = x

    def __repr__(self):
        return str(vars(self))


class SubClass(SuperClass):
    def __init__(self, x):
        SuperClass.__init__(self, x)


thing = SubClass(3)
print(thing)
