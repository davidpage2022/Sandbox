"""Description of a monster"""


class Monster:
    """Description of a monster"""

    def __init__(self, name="Mike", number_of_teeth=0, colour="blue"):
        """Initialize monster with name, number of teeth and a colour."""
        self.name = name
        self.number_of_teeth = number_of_teeth
        self.colour = colour

    def is_scary(self):
        """Determine if monster is "scary" based on teeth and colour."""
        return self.number_of_teeth > 16 or self.colour == "red"


if __name__ == '__main__':
    pass
