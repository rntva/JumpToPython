#!/usr/bin/env python3
import os
import sys
import glob
import pandas as pd

input_directory = sys.argv[1]
output_file = sys.argv[2]

all_work_books = glob.glob(os.path.join(input_directory, "*.xls*"))
data_frames = []

for workbook in all_work_books :
    all_worksheets = pd.read_excel(workbook, sheet_name=None, index_col=None)
    workbook_total_sales = []
    workbook_total_num_of_sales = []
    worksheet_data_frames = []
    worksheets_data_frame = None
    workbook_data_frame = None
    for worksheet_name, data in all_worksheets.items() :
        worksheet_total_sales = pd.DataFrame([float(str(value).strip('$').replace(',', '')) for value in data.ix[ : , "Sale Amount"]]).sum()
        worksheet_num_of_sales = len(data.loc[ : , "Sale Amount"])
        worksheet_average = worksheet_total_sales / worksheet_num_of_sales

        workbook_total_sales.append(worksheet_total_sales)
        workbook_total_num_of_sales.append(worksheet_num_of_sales)

        data = {"workbook" : os.path.basename(workbook),
                "worksheet" : worksheet_name,
                "worksheet_total" : worksheet_total_sales,
                "worksheet_average" : worksheet_average
                }

        worksheet_data_frames.append(pd.DataFrame(data, columns=["workbook", "worksheet", "worksheet_total", "worksheet_average"]))
    worksheets_data_frame = pd.concat(worksheet_data_frames, axis=0, ignore_index=True)

    workbook_total = pd.DataFrame(workbook_total_sales).sum()
    workbook_total_num_of_sales_sum = pd.DataFrame(workbook_total_num_of_sales).sum()
    workbook_average = pd.DataFrame(workbook_total / workbook_total_num_of_sales_sum)

    workbook_stats = {"workbook" : os.path.basename(workbook),
                      "workbook_total" : workbook_total_sales,
                      "workbook_average" : workbook_average
                      }

    workbook_stats = pd.DataFrame(workbook_stats, columns=["workbook", "workbook_total", "workbook_average"])
    workbook_data_frame = pd.merge(worksheets_data_frame, workbook_stats, on="workbook", how="left")
    data_frames.append(workbook_data_frame)

all_data_concat = pd.concat(data_frames, axis=0, ignore_index=True)

writer = pd.ExcelWriter(output_file)
all_data_concat.to_excel(writer, sheet_name="fucking_hard", index=False)
writer.save()

print("End.")