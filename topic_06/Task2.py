import csv

studentList = []

with open("table.csv") as file:
    reader = csv.DictReader(file, skipinitialspace=True)
    for row in reader:
        studentList.append({"name":row["StudentName"], "mark":int(row["StudentMark"])})

print("--- Сортування ---")

for elem in sorted(studentList, key=lambda x: x['mark']):
    print(f"Name = {elem['name']}  mark = {elem['mark']}")