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
median = df.groupby('Drug Regimen').mean()['Tumor Volume (mm3)']
variance = df.groupby('Drug Regimen').median()['Tumor Volume (mm3)']
std_dev = df.groupby('Drug Regimen').var()['Tumor Volume (mm3)']
sem = df.groupby('Drug Regimen').sem()['Tumor Volume (mm3)']

table = pd.DataFrame(
    {'mean': mean, 'median': median, 'variance': variance, 'std_dev': std_dev, 'sem': sem})
table

df['Drug Regimen'].value_counts()

# histogram/bar chart using pandas
num_mice = df['Drug Regimen'].value_counts()
num_mice.plot(kind="bar")

# histogram/bar chart using matplotlib
ticks = [value for value in x_axis]
drug_regimens = df['Drug Regimen'].unique()

# create plot
plt.xticks(ticks, drug_regimens)

plt.pie(num_mice, labels=drug_regimens)
df.Sex.value_counts()

df.Sex.value_counts()
sex_count = df.Sex.value_counts()
df.Sex.unique()
sex = df.Sex.unique()
plt.pie(sex_count.values, labels=sex, autopct='%1.1f%%')

#  final tumor volume of each mouse across the top 4  drug drug_regimens
final_volume = df.loc[df['Timepoint'] == 45].reset_index()
final_volume

final = df.loc[df['Timepoint'] == 45].reset_index()
final = final[['Mouse ID', 'Drug Regimen', 'Tumor Volume (mm3)']]
final = final[(final['Drug Regimen'] == "Capomulin") | (final['Drug Regimen'] == 'Ramicane') | (final['Drug Regimen'] == 'Infubinol') | (final['Drug Regimen'] == 'Ceftamin')].reset_index()
final
