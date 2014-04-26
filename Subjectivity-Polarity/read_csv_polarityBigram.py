#Train: python train_classifier.py --algorithm NaiveBayes --instances files --fraction 0.75 --filename bigr.pickle --min_score 3 --ngrams 2 --show-most-informative 10 movie_reviews

import pickle
import nltk.classify.util
from nltk.util import ngrams
from pandas import DataFrame, read_csv

#Read the tweets from the .csv file
df = read_csv("subjectivity.csv")
tweets = df.text #you can also use df['column_name']
ts = df.ts
userid = df.userid
nb_followers = df.nb_followers


classifier = pickle.load(open("C:/Users/pat/Desktop/IRDM Stock Market and Twitter/newCore/nltk-trainer-master/bigr.pickle"))



#Get the predictions for the tweets using the trained classifier
sentiments = []

count = tweets.count()

for index,tweet in enumerate(tweets):
    percent = float(index)/float(count)
    print "{:4.2f}".format((percent)*100),"%"
    #print '%d/%d' % (index, count)
    words = nltk.word_tokenize(tweet)
    feats = dict([(word, True) for word in words + ngrams(words, 2)])
    temp = classifier.prob_classify(feats).prob('pos')
    sentiments.insert(index,temp)
    


#Export sentiments.csv containing tweets and their predicted sentiments
combined = zip(ts,tweets,sentiments,userid,nb_followers)
df = DataFrame(data = combined, columns = ['ts','text','polarity','userid','nb_followers'])
df.to_csv('bigram_polarity.csv',index=False)

