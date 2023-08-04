import os
import pandas as pd

input_folder = "D:\project_final\csv_output2"
output_folder = "D:\project_final"

all_data = pd.DataFrame()

# iterate
for filename in os.listdir(input_folder):
    if filename.endswith(".csv"):
        input_file_path = os.path.join(input_folder, filename)
        df = pd.read_csv(input_file_path, encoding='utf-8')
        all_data = pd.concat([all_data, df], ignore_index=True)

# save the outcome
output_file_path = os.path.join(output_folder, "合并后的数据.csv")
all_data.to_csv(output_file_path, index=False)

print("Success！")



