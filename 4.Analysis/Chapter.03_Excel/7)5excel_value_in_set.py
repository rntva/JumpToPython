#!/usr/bin/env python3
import sys
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_file = sys.argv[1]
output_file = sys.argv[2]

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet("january_2013_output")

important_dates = ["01/24/2013", "01/31/2013"]

purchase_date_column_index = 4

with open_workbook(input_file) as workbook :
    workseeht = workbook.sheet_by_name("january_2013")
    data = []
    header = workseeht.row_values(0)
    data.append(header)
    for row_index in range(1, workseeht.nrows) :
        row_list = []
        purchase_datetime = xldate_as_tuple(workseeht.cell_value(row_index, purchase_date_column_index), workbook.datemode)
        purchase_date = date(*purchase_datetime[0:3]).strftime("%m/%d/%Y")
        if purchase_date in important_dates :
            for colum_index in range(workseeht.ncols) :
                cell_value = workseeht.cell_value(row_index, colum_index)
                cell_type = workseeht.cell_type(row_index, colum_index)
                if cell_type == 3 :
                    row_list.append(purchase_date)
                    # date_cell = xldate_as_tuple(cell_value, workbook.datemode)
                    # date_cell = date(*date_cell[0:3]).strftime("%m/%d/%Y")
                    # row_list.append(date_cell)
                else : row_list.append(cell_value)
        if row_list : data.append(row_list)

    for list_index, output_list in enumerate(data) :
        for element_index, element in enumerate(output_list) :
            output_worksheet.write(list_index, element_index, element)

output_workbook.save(output_file)

print("End.")

# date_cell = xldate_as_tuple(cell_value, workbook.datemode)
#                     date_cell = date(*date_cell[0:3]).strftime("%m/%d/%y")
#                     row_list.append(date_cell)