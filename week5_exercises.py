"""Week 5 exercises"""

from operator import itemgetter

# data = [['Derek', 7], ['Xavier', 80], ['Bob', 612], ['Chantanelley', 9]]
# name_to_number = {'Derek': 7, 'Xavier': 80, 'Bob': 612, 'Chantanelley': 9}

# name_to_number = {person: score for person, score in data}
# print(name_to_number)

# max_length = max(len(person) for person, score in data)
# for person, score in sorted(data, key=itemgetter(1), reverse=True):
#     print(f"{person:{max_length}} = {score:>3}")

# max_length = max(len(name) for name in name_to_number.keys())
# for name, number in name_to_number.items():
#     print(f"{name:{max_length}} = {number:>3}")


# def main():
#     names = ["Dave", "Susan", "Jane"]
#     ages = [45, 55, 35]
#
#     print(find_oldest(names, ages))


# def find_oldest(names, ages):
#    # return names[ages.index(max(ages))]
#
#    oldest_age = -1
#    oldest_index = -1
#    for i, age in enumerate(ages):
#        if age > oldest_age:
#            oldest_age = age
#            oldest_index = i
#    return names[oldest_index]
#
#    # oldest_person = names[0]
#    # oldest_age = ages[0]
#    # for i in range(len(names)):
#    #     if ages[i] > oldest_age:
#    #         oldest_person = names[i]
#    #         oldest_age = ages[i]
#    # return oldest_person


# main()


# name_to_age = {"Bill": 21, "Jane": 4, "Sven": 56}
# name = input("Enter name: ")
# age = int(input("Enter age: "))
# name_to_age[name] = age
# max_length = max(len(name) for name in list(name_to_age.keys()))
# for name, age in name_to_age.items():
#     print(f"{name:{max_length}} - {age:>6}")


import requests
import json

URL = "https://api.spaceflightnewsapi.net/v3/blogs"

response = requests.get(URL)
data = response.json()

for item in data:
    print(item["title"])

with open("Data/SpaceflightNews-Blogs.json", "w") as out_file:
    json.dump(data, out_file)

    # print("[", file=out_file)
    # for item in data:
    #     line = str(item).replace("'", '"')
    #     print(f"\t{line},", file=out_file)
    # print("]", file=out_file)


