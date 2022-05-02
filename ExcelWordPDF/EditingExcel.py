#! /usr/bin/env python3
import openpyxl
import os

wb = openpyxl.Workbook() #creates a new workbook w/ a single she named 'Sheet'
sheet = wb.get_sheet_by_name('Sheet')

#to edit we can assign values directly to cells

sheet['A1'] = 42

#to save change directory to wherever you would want to save it before
os.chdir('path/to/folder')
wb.save('nameOfFile.xlsx') #save with a different filename if adjusting an existing file just in case
sheet2 = wb.create_sheet() #alternatively just create another sheet and save values there options => title & position


