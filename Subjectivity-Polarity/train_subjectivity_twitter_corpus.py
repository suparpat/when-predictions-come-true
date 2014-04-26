#From: http://streamhacker.com/2010/05/10/text-classification-sentiment-analysis-naive-bayes-classifier/

from pandas import DataFrame, read_csv
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
import numpy as np
 
def word_feats(words):
    return dict([(word, True) for word in words])

#Read the tweets from the .csv file
df = read_csv("trainingandtestdata/testdata.manual.2009.06.14.csv", header=None)

#There are 1,600,000... had a Memory error. So will instead randomize and use 10% of them
ten_percent = len(df)*1
dfran = df.loc[np.random.choice(df.index, ten_percent, replace=False)]

#Add column headers and get only the relevant columns
df2 = DataFrame(data=dfran,columns=[0,5])
df2.columns = ['sentiments','tweets']
tweets = df2.tweets
sentiments = df2.sentiments


neutrals = []
subjectives = []

for x in range(0,len(sentiments)):
    temp = sentiments.iloc[x]
    if temp==2:
        neutrals.append(tweets.iloc[x])
    else:
        subjectives.append(tweets.iloc[x])



     
subfeats = [(word_feats(nltk.word_tokenize(subjectives[x])), 'sub') for x in range(0,len(subjectives))]
neufeats = [(word_feats(nltk.word_tokenize(neutrals[x])), 'neu') for x in range(0,len(neutrals))]
 
subcutoff = len(subfeats)*3/4
neucutoff = len(neufeats)*3/4
 
trainfeats = subfeats[:subcutoff] + neufeats[:neucutoff]
testfeats = subfeats[subcutoff:] + neufeats[neucutoff:]
print 'train on %d instances, test on %d instances' % (len(trainfeats), len(testfeats))

classifier = NaiveBayesClassifier.train(trainfeats)
print 'accuracy:', nltk.classify.util.accuracy(classifier, testfeats)
classifier.show_most_informative_features()

#import pickle
#f = open('my_classifier.pickle', 'wb')
#pickle.dump(classifier, f)
#f.close()

