import os
import pandas as pd

input_folder = "D://微信//WeChat Files//wxid_ilefsgby3fq222//FileStorage//File//2023-07//csv_output"
output_folder = "D://微信//WeChat Files//wxid_ilefsgby3fq222//FileStorage//File//2023-07//csv_sum"
z = 0

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    z += 1
    if filename.endswith(".csv"):
        input_file_path = os.path.join(input_folder, filename)
        output_file_path = os.path.join(output_folder, filename)

        df = pd.read_csv(input_file_path, encoding='cp932')
        df["average"] = df["取引価格（総額）"] / df["面積（㎡）"]

        specified_values = range(2005, 2023)
        avg_values = []

        for value in specified_values:
            avg = df[df['取引時点'] == value]['average'].mean()
            avg_values.append(avg)

        df["avg_sum"] = avg_values

        df.to_csv(output_file_path, index=False)
        print(f"Nuber{z} has been successful！")

print("Success！")






