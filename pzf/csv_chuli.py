import os
import pandas as pd

input_folder = "D:\project_final\csv_output"
output_folder = "D:\project_final\csv_output2"
z = 0

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

all_years = list(range(2006, 2023))
total_missing_count = 0

for filename in os.listdir(input_folder):
    z += 1
    if filename.endswith(".csv"):
        input_file_path = os.path.join(input_folder, filename)
        output_file_path = os.path.join(output_folder, filename)

        df = pd.read_csv(input_file_path, encoding='utf-8')
        df_avg = df.groupby("取引時点")["average"].mean().reset_index()
        df_avg = df_avg.set_index("取引時点").reindex(all_years, fill_value=-1).reset_index()

        missing_years = df_avg[df_avg["average"] == -1]["取引時点"]
        missing_count = len(missing_years)
        total_missing_count += missing_count

        if missing_count > 0:
            print(f"file '{filename}' miss the year：{missing_years.tolist()}")

        df_avg.to_csv(output_file_path, index=False)
        print(f"Number{z}has been succeed！ Missing count: {missing_count}")

print(f"Success！ Total missing count: {total_missing_count}")



