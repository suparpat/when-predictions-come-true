from pandas import DataFrame, read_csv
import pandas as pd
from datetime import datetime, date, time
import math

#Read the .csv file
df = read_csv("intel_bigram_polarity.csv")
ts = df.ts
text = df.text
polarity = df.polarity
userid = df.userid
nb_followers = df.nb_followers
combined = zip(ts,text,polarity,userid,nb_followers)

remove_rows = []
countt = 0
#Remove rows with bad data
for t in range(0,len(ts)):
    for l in combined[t]:
        if pd.isnull(l):
            countt = countt + 1
            remove_rows.append(t)

new_combined = []
for c in range(0,len(combined)):
    if c not in remove_rows:
        new_combined.append(combined[c])

print 'Total of %d rows removed'%countt

#Export sentiments.csv containing tweets and their predicted sentiments
df = DataFrame(data = new_combined, columns = ['ts','text','polarity','userid','nb_followers'])
df.to_csv('cleaned_intel_bigram_polarity.csv',index=False)


