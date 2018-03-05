#!/usr/bin/env python3
import sys
import pandas as pd

input_file = sys.argv[1]
output_file = sys.argv[2]

counting = 1
data_frame = pd.read_excel(input_file, sheet_name="january_2013", index_col=None)
data_frame_value_meets_condition = data_frame[data_frame["Sale Amount"].astype(float) > 1400.0]

writer = pd.ExcelWriter(output_file)
data_frame_value_meets_condition.to_excel(writer, sheet_name="january_2013_output", index=False)
writer.save()

print("End.")