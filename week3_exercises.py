"""Exercises for week 3 lecture"""

# FILENAME = "week2_exercises.py"
#
#
# def main():
#     infile = open(FILENAME)
#     for line in infile:
#         if line[0] == "#":
#             print(line.strip())
#     infile.close()
#
#
# main()

# with open("data_test.csv", "r") as in_file:
#     in_file.readline()  # Ignore header.
#     for line in in_file:
#
#         parts = line.strip().split(',')
#         building = parts[0]
#         cost = float(parts[1])
#
#         # building, cost = line.strip().split(',')
#         # cost = float(cost)
#
#         print(f"{building} costs ${cost:.2f}")


######################################################
# FILENAME = "number.txt"
#
#
# def main():
#     secret = load_number(FILENAME)
#     guess = get_valid_number()
#     while guess != secret:
#         print("Guess again!")
#         guess = get_valid_number()
#     print("You got it!")
#
#
# def get_valid_number():
#     is_valid_input = False
#     while not is_valid_input:
#         try:
#             guess = int(input("Guess: "))
#             is_valid_input = True
#         except ValueError:
#             print("Invalid integer")
#     return guess
#
#
# def load_number(filename):
#     try:
#         infile = open(filename, "r")
#         number = int(infile.read())
#     except ValueError:
#         print(f"Invalid contents in {filename}")
#         number = 6
#     except FileNotFoundError:
#         print(f"{filename} not found")
#         number = 4
#     else:
#         infile.close()
#     return number
#
#
# main()
######################################################


# Printing number of errors

# number_of_errors = 0
# ...
#     exception ...:
#         number_of_errors += 1
# ...
# if number_of_errors > 0:
#     print(f"There were {number_of_errors} errors")

# Use a list

#
# name = input("Name: ")
# with open("name.txt", "w") as out_file:
#     print(name, file=out_file)


names = ["Larry", "Joe", "Jane"]

for i, name in enumerate(names, 1):
    with open(name + ".txt", "w") as out_file:
        print(name, file=out_file)
        print(i, file=out_file)


