import csv
import pandas as pd
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

from calendar import day_name


plt.figure(figsize=(11,8))
file = 'police_reports_output/part-00000.csv'
df = pd.read_csv(file, sep="\t", header=None)
df.columns = ["Days", "Number of Incident"]
df = df.reindex([1, 5, 6, 4, 0, 2, 3])

plt.bar(df['Days'], df['Number of Incident'], color='blue', width=.5, align='center')
plt.xticks(rotation=45)
plt.title("Crime Incidents By Days")
plt.savefig('./incidents_vs_days.png')
