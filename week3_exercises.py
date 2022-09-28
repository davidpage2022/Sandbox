"""Exercises for week 3 lecture"""
FILENAME = "week2_exercises.py"


def main():
    infile = open(FILENAME)
    for line in infile:
        if line[0] == "#":
            print(line.strip())
    infile.close()


main()
