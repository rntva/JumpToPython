#!/usr/bin/env python3
import sys
import pandas as pd

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_excel(input_file, "january_2013", index_col=None)

important_date = ["01/24/2013", "01/31/2013"]
data_frame_value_in_set = data_frame[data_frame["Purchase Date"].isin(important_date)]

writer = pd.ExcelWriter(output_file)
data_frame_value_in_set.to_excel(writer, sheet_name="january_2013_output", index=False)
writer.save()

print("End.")