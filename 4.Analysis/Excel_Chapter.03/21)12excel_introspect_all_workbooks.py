#!usr/bin/env python3
import os
import sys
import glob
from xlrd import open_workbook

input_directory = sys.argv[1]

workbook_counter = 0
for input_file in glob.glob(os.path.join(input_directory, "*.xls*")) :
    workbook = open_workbook(input_file)
    print("Workbook : {}".format(os.path.basename(input_file)))
    print("Number of Worksheet : {}".format(workbook.nsheets))
    for worksheet in workbook.sheets() :
        print("Worksheet name : ", worksheet.name, "\tRows\t : ", worksheet.nrows, "\tCols\t : ", worksheet.ncols)
    workbook_counter += 1
print("Number of Excel Workbooks : {}".format(workbook_counter))

print("End.")




