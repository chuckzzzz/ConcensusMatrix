import matplotlib.pyplot as plt
from numpy import genfromtxt
import pandas as pd
import numpy as np

path = "/mnt/silencer2/home/ziz361/data/consensus_matrix_data/cs_random1.csv"
percentile = 0.001
image_path = "/mnt/silencer2/home/ziz361/data/consensus_matrix_data/cs_random1_plot.csv"

# remove redundant values from the consensus matrix as it is symmetric 
# flatten data afterwards 
# remove 0 entries in the flattened data 
def df_preprocess(df):
    df = df.astype(float)
    df.values[np.triu_indices_from(df, k=1)] = np.nan
    df = df.unstack().dropna()
    flattened_data = df.ravel()
    flattened_data = flattened_data[flattened_data!=0]
    print("Total data points: {}".format(len(flattened_data)))
    return flattened_data

data = genfromtxt(path, delimiter = ',')
df = pd.DataFrame(data)
df.values[tuple([np.arange(df.shape[0])]*2)] = 0 #set diaganol value to 0 for removal
cs_data = df_preprocess(df)

_ = plt.hist(cs_data, bins = "auto")
plt.title("Histogram for consensus matrix")
plt.xlabel("Normalized consensus count")
plt.ylabel("Frequency")
plt.savefig(image_path)
cs_data_np = np.array(cs_data)
threshold = np.percentile(cs_data_np, percentile)
print("Calculated threshold is: {}".format(threshold))