"""Week 2 menu exercise
menu:
- get valid (non-empty) name
- print greeting with lines
- print secret name (random variation)
"""
import random

MENU = """(N)ame
(G)reeting
(S)ecret name
(Q)uit"""


def main():
    name = "stranger"
    print(MENU)
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "N":
            name = get_valid_name()
            print(name)
        elif choice == "G":
            print_greeting(name)
        elif choice == "S":
            print_secret_name(name)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>>").upper()
    print("Thank you")


def get_valid_name():
    name = input("Enter name: ")
    while name == "":
        print("Invalid name")
        name = input("Enter name: ")
    return name


def print_greeting(name):
    greeting = "Hello "
    i = len(name) + len(greeting)
    print_line(i)
    print(f"{greeting}{name}")
    print_line(i)


def print_line(length):
    print("-" * length)


def print_secret_name(name):
    letters = list(name)
    random.shuffle(letters)
    print("".join(letters))


def get_new_secret_name():
    first_names = ["John", "Jane", "Larry", "Mary", "Alexander"]
    second_names = ["Smith", "Doe", "King", "Queen", "Monroe"]
    return f"{random.choice(first_names)} {random.choice(second_names)}"


main()
