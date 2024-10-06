import csv

file = "Data/unlabelled_data.csv"

with open ("Data/unlabelled_data.csv", "r") as file:
    reader = csv.reader(file)
    for lines in csvFile:
        print(lines)
