import openpyxl
import process_data
from openpyxl.styles import PatternFill
import time
from datetime import datetime

file_prefix = datetime.now().strftime("%d-%m-%Y_%H:%M:%S_")
output_dir = "output"

def file_path(file = ""):
    return output_dir + "/"+file_prefix + file + ".xlsx"

def create_workbook(version = 'a'):
    wb = openpyxl.Workbook() 
    ws = wb.active
    ws = wb['Sheet']
    ws.title = "diff"
    ws_sp = wb.create_sheet("sp") 
    ws_ps = wb.create_sheet("ps") 
    ws.sheet_properties.tabColor = "dba281"
    ws_sp.sheet_properties.tabColor = "99c39e"
    ws_ps.sheet_properties.tabColor = "89cdd3"
    workbook.save(filename = file_path(version))
    return wb

wb = create_workbook()

def load_workbook(version = 'a'):
    return openpyxl.load_workbook(file_path('a'))

def export_row(row, sheet, workbook, version = 'a'):
    workbook[sheet].append(row)
    workbook.save(filename = file_path(version))

export_row([1,2,3,4,5], 'sp', wb)
export_row([2,2,3,4,5], 'sp', wb)
export_row([3,2,3,4,5], 'sp', wb)

def diff_sheet(sheet, workbook, version = 'a'):
    for row in workbook[sheet]:
        for cell in row:
            workbook['diff'][cell.coordinate].value = cell.value
    workbook.save(filename = file_path(version))

diff_sheet('sp', wb)
