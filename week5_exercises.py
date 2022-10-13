"""Week 5 exercises"""

data = [['Derek', 7], ['Xavier', 80], ['Bob', 612], ['Chantanelley', 9]]

max_length = 0
for person, score in data:
    if len(person) > max_length:
        max_length = len(person)
for person, score in data:
    print(f"{person:{max_length}} = {score:>3}")
