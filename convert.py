import csv
import openpyxl

wb = openpyxl.Workbook()
ws = wb.active

with open('output/example.csv') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        ws.append(row)

wb.save('file.xlsx')
