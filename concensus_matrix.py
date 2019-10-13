import os
import pandas as pd
target_dir = ".\cluster_data"
data_path_list = list()
for root, dirs, files in os.walk(target_dir):
    for file in files:
        if file.endswith(".csv"):
            data_path_list.append(os.path.join(root, file))
print(data_path_list)
for path in data_path_list:
    df = pd.read_csv(path)
    print(len(df))