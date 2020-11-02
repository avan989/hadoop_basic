import csv
import pandas as pd
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

from calendar import day_name


plt.figure(figsize=(11,8))
file = 'police_reports_output/part-00000.csv'
df = pd.read_csv(file, sep="\t", header=None)
df.columns = ["time", "Number of Incident"]
df = df.reindex([0, 1, 12, 17, 18, 19, 20, 21, 22, 23, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16])

plt.bar(df['time'], df['Number of Incident'], color='blue', width=.5, align='center')
plt.xticks(rotation=45)
plt.title("Crime Incidents By Hours")
plt.savefig('./incidents_vs_hours.png')

value = df.sort_values(by="Number of Incident")
plt.clf()
plt.bar(value['time'], value['Number of Incident'], color='blue', width=.5, align='center')
plt.xticks(rotation=45)
plt.title("Crime Incidents By Hours")
plt.savefig('./incidents_vs_hours_order_by_incident.png')