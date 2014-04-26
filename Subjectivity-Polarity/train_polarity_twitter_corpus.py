#From: http://streamhacker.com/2010/05/10/text-classification-sentiment-analysis-naive-bayes-classifier/

from pandas import DataFrame, read_csv
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
import numpy as np
 
def word_feats(words):
    return dict([(word, True) for word in words])

#Read the tweets from the .csv file
df = read_csv("trainingandtestdata/training.1600000.processed.noemoticon.csv", header=None)

#There are 1,600,000... had a Memory error. So will instead randomize and use 10% of them
ten_percent = len(df)*0.1
dfran = df.loc[np.random.choice(df.index, ten_percent, replace=False)]

#Add column headers and get only the relevant columns
df2 = DataFrame(data=dfran,columns=[0,5])
df2.columns = ['sentiments','tweets']
tweets = df2.tweets
sentiments = df2.sentiments


neutrals = []
positives = []
negatives = []
for x in range(0,len(sentiments)):
    temp = sentiments.iloc[x]
    if temp==0:
        negatives.append(tweets.iloc[x])
    elif temp==2:
        neutrals.append(tweets.iloc[x])
    else:
        positives.append(tweets.iloc[x])
        

posfeats = [(word_feats(nltk.word_tokenize(positives[x])), 'pos') for x in range(0,len(positives))]
negfeats = [(word_feats(nltk.word_tokenize(negatives[x])), 'neg') for x in range(0,len(negatives))]
 
poscutoff = len(posfeats)*3/4
negcutoff = len(negfeats)*3/4
 
trainfeats = posfeats[:poscutoff] + negfeats[:negcutoff]
testfeats = posfeats[poscutoff:] + negfeats[negcutoff:]
print 'train on %d instances, test on %d instances' % (len(trainfeats), len(testfeats))

classifier = NaiveBayesClassifier.train(trainfeats)
print 'accuracy:', nltk.classify.util.accuracy(classifier, testfeats)
classifier.show_most_informative_features()

#import pickle
#f = open('my_classifier.pickle', 'wb')
#pickle.dump(classifier, f)
#f.close()

