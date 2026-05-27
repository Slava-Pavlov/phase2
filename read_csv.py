import csv
with open("people.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row["name"]} from {row["city"]} is {row["age"]}")