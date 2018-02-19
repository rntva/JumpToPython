#!/usr/bin/env python3
import sys
import pandas as pd

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_excel(input_file, sheet_name=None, index_col=None)

row_output = []
for worksheet_name, data in data_frame.items() :
    row_output.append(data.loc[ : , ["Customer Name", "Sale Amount"]])
filtered_rows = pd.concat(row_output, axis=0, ignore_index=True)

writer = pd.ExcelWriter(output_file)
filtered_rows.to_excel(writer, sheet_name="filtered_rows_all_worksheet", index=False)
writer.save()

print("End.")
