#!/urs/bin/env python3
import os
import sys
import glob
import pandas as pd

input_directory = sys.argv[1]
output_file = sys.argv[2]

all_workbook = glob.glob(os.path.join(input_directory, "*.xls*"))
data_frames = []
for workbook in all_workbook :
    all_worksheet = pd.read_excel(workbook, sheet_name=None, index_col=None)
    for worksheet_name, data in all_worksheet.items() :
        data_frames.append(data)
all_data_concat = pd.concat(data_frames, axis=0, ignore_index=True)

writer = pd.ExcelWriter(output_file)
all_data_concat.to_excel(writer, sheet_name="all_workbook_concat", index=False)
writer.save()

print("End.")

