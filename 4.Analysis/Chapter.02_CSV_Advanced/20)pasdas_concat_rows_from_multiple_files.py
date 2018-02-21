#!/usr/bin/env python3
import os
import sys
import glob
import pandas as pd

input_path = sys.argv[1]
output_file = sys.argv[2]

all_files = glob.glob(os.path.join(input_path, "sales_*"))

all_data_frames = []
for file in all_files :
    data_frame = pd.read_csv(file)
    all_data_frames.append(data_frame)
data_frame_concat = pd.concat(all_data_frames, axis=0, ignore_index=True)
data_frame_concat.to_csv(output_file, index=False)

print("End.")