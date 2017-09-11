import pandas as pd
import datetime
from collections import defaultdict

path_to_file = "/Users/swaroop/Downloads/Folder1/Issues.csv"
df = pd.read_csv(path_to_file)

groups = df.groupby(['Category', 'Opened'])
max_for_issue = defaultdict(int) #first pass through the groups, store the maximum for each issue to handle ties

for g in groups:
    issue, count = g[0][0], len(g[1])
    max_for_issue[ issue ] = max( max_for_issue[issue], count )

for g in groups:
    issue, state, count = g[0][0], g[0][1], len(g[1])
    if count == max_for_issue[ issue ]:
        print( "{} {} {}".format(issue, state, count ) )


# df = pd.read_csv("/Users/swaroop/Downloads/Folder1/datetime.csv",  usecols=[1])
# # print df
# df['Column-2'] = df['Column-2'].dt.strftime('%m/%Y')
# for row in df.iterrows():
# 	print row[1]
# # df.to_csv("/Users/swaroop/Downloads/Folder1/datetime1.csv", sep='\t')        