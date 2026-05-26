people = [{"name": "Max", "age": 25, "city": "Paris", "occupation": "student"}, {"name": "John", "age": 30, "city": "NY", "occupation": "trader"}, {"name": "Julia", "age": 44, "city": "Rome", "occupation": "enrepreneur"}]
for person in people:
    print(f"{person["name"]} is {person["age"]} and lives in {person["city"]}")