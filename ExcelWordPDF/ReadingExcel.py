#! /usr/bin/env python3
from tkinter.tix import COLUMN
import openpyxl
import os

os.chdir('c://path/to/file')

workbook = openpyxl.load_workbook("example.xlsx")
sheet =  workbook.get_sheet_by_name("Sheet1")
sheets = workbook.get_sheet_names()
cell = sheet['A1']
value = cell.value
othercell = sheet.cell(row=1,column=1) #same thing as above but easoier to use in loops to replace ints with an iterator
