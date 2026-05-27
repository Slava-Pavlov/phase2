import csv

people = [{"name": "Max", "age": 25, "city": "Paris", "occupation": "student"}, {"name": "John", "age": 30, "city": "NY", "occupation": "trader"}, {"name": "Julia", "age": 44, "city": "Rome", "occupation": "enrepreneur"}]

with open("output.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name","age","city","occupation"])
    writer.writeheader()
    for person in people:
        writer.writerow(person)