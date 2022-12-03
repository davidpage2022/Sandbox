class SuperClass:
    def __init__(self, x):
        self.x = x

    def __repr__(self):
        return str(vars(self))


class SubClass(SuperClass):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


thing = SubClass(x=3)
print(thing)
