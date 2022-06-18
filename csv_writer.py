import csv

print("Write CSV file using csv.writer...")

with open("data/example.csv", "w") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["1", "first", "example", "row"])
    csv_writer.writerow(["2", "second", "example", "row"])
    csv_writer.writerow(["3", "third", "example", "row"])

print("Write CSV file using DictWriter class...")

with open("data/example_dict_writer.csv", "w") as csv_file:
    fieldnames = ["id", "first_column", "second_column", "third_column"]
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writerow({"id": "1", "first_column": "first", "second_column": "example", "third_column": "row"})
    csv_writer.writerow({"id": "2", "first_column": "second", "second_column": "example", "third_column": "row"})
    csv_writer.writerow({"id": "3", "first_column": "third", "second_column": "example", "third_column": "row"})
