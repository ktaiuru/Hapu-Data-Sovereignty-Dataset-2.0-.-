#!python3
# converttocsv.py - turn excel file to csv

import openpyxl
import csv

excel_file = 'Hapū Data Sovereignty Dataset v20.xlsx'
csv_file = 'Hapū Data Sovereignty Dataset v20.csv'
wb = openpyxl.load_workbook(excel_file)
sh = wb.active
with open(csv_file, 'w', newline="") as f:
    c = csv.writer(f)
    for r in sh.rows:
        c.writerow([cell.value for cell in r])
