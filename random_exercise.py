"""Ask user for a length, then generate a random width between 1 and length."""
import random


def main():
    length = int(input("Length: "))
    width = random.randint(1, length)
    area = length * width
    print(f"Area of {length} x {width} is {area}")


main()
