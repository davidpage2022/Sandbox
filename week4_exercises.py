"""Week 4 exercises"""

# names = ["Dave", "Page", "Craig", "Me"]
#
# is_valid_choice = False
# while not is_valid_choice:
#     try:
#         number = int(input(f"Select name to display (1-{len(names)}): "))
#         # assert choice > 0
#         if number <= 0:
#             raise IndexError()
#         print(names[number - 1])
#         is_valid_choice = True
#     except IndexError:
#         print(f"Choice must be a valid number")
#     # except AssertionError:
#     #     print(f"Choice must be a valid number")


from operator import itemgetter

score_pairs = [['Derek', 7], ['Carrie', 8], ['Bob', 6]]

parts = input("Enter name and score (e.g. \"Dave 5\"): ").split()
name = parts[0]
score = int(parts[1])

score_pairs.append([name, score])
score_pairs.sort(key=itemgetter(1), reverse=True)

print(score_pairs)

