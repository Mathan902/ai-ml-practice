import csv

with open('/Users/softsuave/ai-ml-practice/assets/employees.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)