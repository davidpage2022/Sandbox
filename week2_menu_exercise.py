"""Week 2 menu exercise"""
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
            name = get_secret_name()
            print(name)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>>").upper()


def get_valid_name():
    name = input("Enter name: ")
    while name == "":
        print("Invalid name")
        name = input("Enter name: ")
    return name


def print_greeting(name):
    print(f"Hello {name}!")
    for character in name:
        print(character)
    print("-------------------------------------")


def get_secret_name():
    first_names = [ "John", "Jane", "Larry", "Mary", "Alexander" ]
    second_names = [ "Smith", "Doe", "King", "Queen", "Monroe" ]
    return f"{random.choice(first_names)} {random.choice(second_names)}"


main()
