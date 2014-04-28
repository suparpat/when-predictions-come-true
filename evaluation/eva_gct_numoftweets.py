import numpy as np
import pandas as pd
import statsmodels.tsa.stattools as stat
#import pprint as pp
#from pandas import DataFrame, read_csv
# read csv instances
reader = pd.read_csv("dailytweets.csv")
#day
day = reader.day;

#numberOfTweets
numOfTweets = reader.tweets;
#print numOfTweets;

#avgSentiment
reader2 = pd.read_csv("sentiment.csv")
avgSentiment = reader2.daily_sentiments;
#print avgSentiment;

#joint array
X= np.vstack(([avgSentiment.T], [numOfTweets.T])).T
#lagged operations from 1 to 10, as 11 causes value error
maxlag = 10
#perform a causality test and print 
d=stat.grangercausalitytests(X,maxlag,True,True)




    