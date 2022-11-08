import json

import datetime

class Thing:
    def __init__(self, parent=None):
        self.parent = parent


def main():
    parent = Thing()
    child = Thing(parent)

    date = datetime.date.today()
    print(date.__dict__)

    print(json.dumps(vars(parent), default=vars))
    print(json.dumps(vars(child), default=vars))


if __name__ == '__main__':
    main()
