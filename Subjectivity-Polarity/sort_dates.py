from pandas import DataFrame, read_csv
from datetime import datetime, date, time

#Read the .csv file
df = read_csv("polarity.csv")
ts = df.ts
text = df.text
polarity = df.polarity
userid = df.userid
nb_followers = df.nb_followers
combined = zip(ts,text,polarity,userid,nb_followers)



#Sort
sorted_combined = sorted(combined, key = lambda row: datetime.strptime(row[0],"%a %b %d %H:%M:%S +0000 %Y"))




#Export sorted_polarity.csv
df = DataFrame(data = sorted_combined, columns = ['ts','text','polarity','userid','nb_followers'])
df.to_csv('sorted_polarity.csv',index=False)
