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


with open("data_test.csv", "r") as in_file:
    in_file.readline()  # Ignore header.
    for line in in_file:

        parts = line.strip().split(',')
        building = parts[0]
        cost = float(parts[1])

        # building, cost = line.strip().split(',')
        # cost = float(cost)

        print(f"{building} costs ${cost:.2f}")
