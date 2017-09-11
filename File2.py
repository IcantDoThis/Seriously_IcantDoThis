import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df = pd.read_csv("/Users/swaroop/Downloads/Folder1/IssueType - IssueType.csv",sep=",")
df.index = pd.to_datetime(df["DateTime"])
del df["DateTime"]
list=[]
for Issue in df["Issue Type"]:
    list.append(int(Issue[5:]))
df["Issue_number"]=list

fig, ax = plt.subplots()
ax.plot(df.index,df["Issue_number"])
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m'))
plt.show()