#From: http://streamhacker.com/2010/05/10/text-classification-sentiment-analysis-naive-bayes-classifier/

import nltk.classify.util
from nltk.classify import NaiveBayesClassifier

 
def word_feats(words):
    return dict([(word, True) for word in words])


#Load subjective lines into a list
s = open('subjectivity_corpus/quote.tok.gt9.5000', 'r')
subtxt = s.readlines()
 
#Load neutral lines into a list
n = open('subjectivity_corpus/plot.tok.gt9.5000', 'r')
neutxt = n.readlines()

 
subfeats = [(word_feats(nltk.word_tokenize(subtxt[x])), 'sub') for x in range(0,len(subtxt))]
neufeats = [(word_feats(nltk.word_tokenize(neutxt[x])), 'neu') for x in range(0,len(neutxt))]
 
subcutoff = len(subfeats)*3/4
neucutoff = len(neufeats)*3/4
 
trainfeats = subfeats[:subcutoff] + neufeats[:neucutoff]
testfeats = subfeats[subcutoff:] + neufeats[neucutoff:]
print 'train on %d instances, test on %d instances' % (len(trainfeats), len(testfeats))
 
classifier = NaiveBayesClassifier.train(trainfeats)
print 'accuracy:', nltk.classify.util.accuracy(classifier, testfeats)
classifier.show_most_informative_features()
