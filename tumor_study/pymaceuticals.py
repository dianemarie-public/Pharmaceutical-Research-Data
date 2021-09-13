# Import dependencies
from matplotlib import pyplot as plt
from scipy import stats
import numpy as np
import pandas as pd

# Load data into pandas
tumor_data = pd.read_csv("data/Study_results.csv")
metadata = pd.read_csv("data/mouse_metadata.csv")

tumor_data
# len(tumor_data['Mouse ID'])
len(tumor_data['Mouse ID'].unique())
tumor_data['Timepoint']

tumor_data = tumor_data.drop_duplicates(subset=['Mouse ID', 'Timepoint'])
tumor_data

df = pd.merge(tumor_data, metadata, how="left", on="Mouse ID")
df

mean = df.groupby('Drug Regimen').mean()['Tumor Volume (mm3)']
# mean_vol

median = df.groupby('Drug Regimen').mean()['Tumor Volume (mm3)']
variance = df.groupby('Drug Regimen').median()['Tumor Volume (mm3)']
std_dev = df.groupby('Drug Regimen').var()['Tumor Volume (mm3)']
sem = df.groupby('Drug Regimen').sem()['Tumor Volume (mm3)']

table = pd.DataFrame({'mean': mean, 'median': median, 'variance': variance, 'standard deviation': std_dev, 'sem': sem})
table



id = np.arange(len(id))

plt.bar(regimen, id)
