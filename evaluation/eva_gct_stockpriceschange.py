import numpy as np
import pandas as pd
import statsmodels.tsa.stattools as stat
#import pprint as pp
#from pandas import DataFrame, read_csv
# read csv instances
reader = pd.read_csv("stockprices.csv")
#day
day = reader.Date;

reader2 = pd.read_csv("sentiment.csv")
avgSentiment = reader2.daily_sentiments;
day2 = list(reader2.day);

#format the date
for x in range (0,len(day)):
    day[x] = day[x].replace("-0","-")
    day[x] = day[x].replace("-"," ")
    day[x] = ' '.join(reversed(day[x].split()))
day = list(day)

#closeStockPrice
closeStockPrice = reader.Close;

#changesOfStockPrice
openStockPrice = reader.Open;
changesOfStockPrice = openStockPrice - closeStockPrice;

#joint changes of prices and averaged sentiment into a new 2D array by containing days
newlist = set(day) & set(day2)
newlist = list(newlist)

priceChange = []
avgSenti = []

for i in range(0,len(newlist)):
    x = newlist[i]
    if x in day:
        if x in day2:
            x = str(x)
            i = day.index(x)
            j = day2.index(x)
            priceChange.append(changesOfStockPrice[i])           
            avgSenti.append(avgSentiment[j])
			
X= np.vstack(([np.array(priceChange).T], [np.array(avgSenti).T])).T
#lagged operations from 1 to 7, as 8 causes value error
maxlag = 7
#perform a causality test and print 
d=stat.grangercausalitytests(X,maxlag,True,True)         

    
    
         
