#!/usr/bin/env python3
import sys
import pandas as pd

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_excel(input_file, "january_2013", index_col=None)

data_frame_column_by_name = data_frame.loc[ : , ["Customer ID", "Purchase Date"]]

writer = pd.ExcelWriter(output_file)
data_frame_column_by_name.to_excel(writer, sheet_name="january_2013_output", index=False)
writer.save()

print("End.")
