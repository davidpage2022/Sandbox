"""Week 5 exercises"""

from operator import itemgetter

# data = [['Derek', 7], ['Xavier', 80], ['Bob', 612], ['Chantanelley', 9]]
name_to_number = {'Derek': 7, 'Xavier': 80, 'Bob': 612, 'Chantanelley': 9}

# name_to_number = {person: score for person, score in data}
# print(name_to_number)

# max_length = max(len(person) for person, score in data)
# for person, score in sorted(data, key=itemgetter(1), reverse=True):
#     print(f"{person:{max_length}} = {score:>3}")

max_length = max(len(name) for name in name_to_number.keys())
for name, number in name_to_number.items():
    print(f"{name:{max_length}} = {number:>3}")
