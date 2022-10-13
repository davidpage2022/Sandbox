"""Week 5 exercises"""

data = [['Derek', 7], ['Xavier', 80], ['Bob', 612], ['Chantanelley', 9]]

max_length = max(len(person) for person, score in data)
for person, score in data:
    print(f"{person:{max_length}} = {score:>3}")
