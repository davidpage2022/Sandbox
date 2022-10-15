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


# from operator import itemgetter
#
# score_pairs = [['Derek', 7], ['Carrie', 8], ['Bob', 6]]
#
# parts = input("Enter name and score (e.g. \"Dave 5\"): ").split()
# name = parts[0]
# score = int(parts[1])
#
# score_pairs.append([name, score])
# score_pairs.sort(key=itemgetter(1), reverse=True)
#
# print(score_pairs)


# text = "This is a sentence"
#
# long_words = [word for word in text.split() if len(word) > 3]
#
# print(long_words)


def process_query_string(query):


def main():
    string = "?name=Bob&age=99&day=Wed"

    pairs = extract_pairs(string)
    print(pairs)


def extract_pairs(string):
    """Extract name-value pairs as tuples in a list from a query string."""
    pairs = []
    parts = string[1:].split("&")
    for part in parts:
        pair = part.split("=")
        try:
            pairs.append(tuple((pair[0], int(pair[1]))))
        except ValueError:
            pairs.append(tuple(pair[0]))
    return pairs

# def process_query_string(query):
#     args = query[1:].split("&")
#     pairs = [tuple(arg.split("=")) for arg in args]
#     for i, pair in enumerate(pairs):
#         if pair[1].isnumeric():
#             pairs[i] = (pair[0], int(pair[1]))
#     return pairs


# query_string = "?name=Bob&age=99&day=Wed"

# print(process_query_string(query_string))
