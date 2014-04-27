import collections
import nltk.classify.util, nltk.metrics
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
from pandas import DataFrame, read_csv
import numpy as np
import itertools
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
 

#Read the tweets from the .csv file
df = read_csv("trainingandtestdata/training.1600000.processed.noemoticon.csv", header=None)

#There are 1,600,000... had a Memory error. So will instead randomize and use 10% of them
ten_percent = len(df)*0.05
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


def bigram_word_feats(words, score_fn=BigramAssocMeasures.chi_sq, n=200):
    bigram_finder = BigramCollocationFinder.from_words(words)
    bigrams = bigram_finder.nbest(score_fn, n)
    return dict([(ngram, True) for ngram in itertools.chain(words, bigrams)])

 
negfeats = [(bigram_word_feats(nltk.word_tokenize(negatives[f])), 'neg') for f in range(0,len(negatives))]
posfeats = [(bigram_word_feats(nltk.word_tokenize(positives[f])), 'pos') for f in range(0,len(positives))]
 
negcutoff = len(negfeats)*3/4
poscutoff = len(posfeats)*3/4
 
trainfeats = negfeats[:negcutoff] + posfeats[:poscutoff]
testfeats = negfeats[negcutoff:] + posfeats[poscutoff:]
 
classifier = NaiveBayesClassifier.train(trainfeats)
refsets = collections.defaultdict(set)
testsets = collections.defaultdict(set)
 
for i, (feats, label) in enumerate(testfeats):
        refsets[label].add(i)
        observed = classifier.classify(feats)
        testsets[observed].add(i)
 
print 'accuracy:', nltk.classify.util.accuracy(classifier, testfeats)
print 'pos precision:', nltk.metrics.precision(refsets['pos'], testsets['pos'])
print 'pos recall:', nltk.metrics.recall(refsets['pos'], testsets['pos'])
print 'neg precision:', nltk.metrics.precision(refsets['neg'], testsets['neg'])
print 'neg recall:', nltk.metrics.recall(refsets['neg'], testsets['neg'])
classifier.show_most_informative_features()
