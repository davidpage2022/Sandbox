"""Week 4 exercises during meet up"""


# names = ["Ada", "Alan", "Bill", "John"]
# print(", ".join(names))
# name_to_remove = input("Who do you want to remove?")
# while name_to_remove != "":
#     try:
#         names.remove(name_to_remove)
#     except ValueError:
#         print(f"{name_to_remove} is not in the list")
#     print(", ".join(names))
#     name_to_remove = input("Who do you want to remove?")


# Good
# oo
# T1G1
# 20  ?
#


# 33


# 1. numbers
# 2. number_of_people
# 3. person_age        <---- Don't need person if there are no other types of age.
# 4. points
# 5. is_person_mutant  <---- Don't need person, as above
# 6. i


def main():
    numbers = get_numbers()
    square_numbers(numbers)
    display_numbers(numbers)


def get_numbers():
    user_input = "1,4.5,90, -2, 8,2"  # input("Enter numbers separated by commas: ")
    is_input_valid = False
    while not is_input_valid:
        try:
            numbers = [float(x) for x in user_input.split(",")]
            is_input_valid = True
        except ValueError:
            print("Invalid number entered")
            user_input = input("Enter numbers separated by commas: ")
    return numbers


def square_numbers(numbers):
    for i, number in enumerate(numbers):
        numbers[i] = number ** 2


def display_numbers(numbers):
    numbers.sort()
    formatted_numbers = [f"{number:.1f}" for number in numbers]
    print("..".join(formatted_numbers))


main()
