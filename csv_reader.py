import csv

print("Read file using csv.reader...")

# read laptop.csv using csv.reader
with open("data/laptop.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        print(row)

print("Read file using DictReader class...")

with open("data/laptop.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        print(row)
