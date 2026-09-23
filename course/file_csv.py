import csv

data = [
    ['Name', 'Age', 'City'],
    ['Alice', '30', 'New York'],
    ['Bob', '25', 'Los Angeles']
]

dictData = [
    {'Name': 'Alice', 'Age': '30', 'City': 'New York'},
    {'Name': 'Bob', 'Age': '25', 'City': 'Los Angeles'}
]

with open("dict-csv.csv", mode="w", newline="") as f:
    fieldNames = ["Name", "Age", "City"]
    csv_dictWriter = csv.DictWriter(f, fieldnames=fieldNames)
    csv_dictWriter.writeheader()
    csv_dictWriter.writerows(dictData)

with open("dict-csv.csv", mode="r") as f:
    csv_dictReader = csv.DictReader(f)
    for row in csv_dictReader:
        print(row)


with open("csv.csv", mode="w", encoding="utf-8", newline="") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerows(data)

with open("csv.csv", mode="r") as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        print(row)


