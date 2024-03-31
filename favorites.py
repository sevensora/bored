import csv

from collections import Counter

with open("favorites.csv", "r") as file:

    reader = csv.DictReader(file)

    counts = Counter()

    for row in reader:
        favourite = row["problem"]
        counts[favorite] += 1

favorite = input("Favorite: ")
print(f"{favorite}: {counts[favorite]}")
