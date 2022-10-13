"""Week 5 exercises"""

from operator import itemgetter

data = [['Derek', 7], ['Xavier', 80], ['Bob', 612], ['Chantanelley', 9]]

max_length = max(len(person) for person, score in data)
for person, score in sorted(data, key=itemgetter(1), reverse=True):
    print(f"{person:{max_length}} = {score:>3}")
