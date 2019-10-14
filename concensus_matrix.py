import os
import pandas as pd
import numpy as np

###### INPUT HERE #####
target_dir = ".\cluster_test_data"
###### INPUT HERE #####

data_path_list = list()
for root, dirs, files in os.walk(target_dir):
    for file in files:
        if file.endswith(".csv"):
            data_path_list.append(os.path.join(root, file))
print("Total file found: {}".format((str(len(data_path_list)))))

# read the first file to get the size of concensis matrix 
path = data_path_list[0]
df = pd.read_csv(path)
concensus_matrix = np.zeros((len(df), len(df)))

#loop through all the data files found 
counter = 0
for path in data_path_list:
    if(counter != 0):
        print("{}/{} finished!".format(counter, len(data_path_list)))
    df = pd.read_csv(path)
    df.columns = ['cluster']
    num_cluster = df.max().values[0]
    cluster_cell_dict = {}
    
    # instantiate the dictionary
    for idx in range(num_cluster):
        cluster_cell_dict[idx+1] = []
    cell_count = 0

    # store cells by cluster
    for idx, row in df.iterrows():
        cell_cluster = row['cluster']
        cluster_cell_dict[cell_cluster].append(cell_count)
        cell_count += 1

    # loop through the separated cells and add count to concensus matrix 
    for key, values in cluster_cell_dict.items():
        cur_freq_matrix = values
        for outer in cur_freq_matrix:
            for inner in cur_freq_matrix:
                concensus_matrix[outer][inner] += 1
    counter += 1
#Normalize the concensus matrix 
print("{}/{} finished!".format(counter, len(data_path_list)))
concensus_matrix = concensus_matrix / len(data_path_list)
print("Writing normalized concensus matrix to concensus_matrix.csv")
np.savetxt("concensus_matrix.csv", concensus_matrix, fmt="%f", delimiter=',')