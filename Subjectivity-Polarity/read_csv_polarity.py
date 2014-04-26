from pandas import DataFrame, read_csv
import train_polarity


#Read the tweets from the .csv file
df = read_csv("subjectivity.csv")
tweets = df.text #you can also use df['column_name']
ts = df.ts
userid = df.userid
nb_followers = df.nb_followers


#Train the Naive Bayes classifier with movie reviews corpus
train_polarity



#Get the predictions for the tweets using the trained classifier
sentiments = []

count = tweets.count()

for index,tweet in enumerate(tweets):
    percent = float(index)/float(count)
    print "{:4.2f}".format((percent)*100),"%"
    #print '%d/%d' % (index, count)
    
    temp = train_polarity.classifier.prob_classify(train_polarity.word_feats(train_polarity.nltk.word_tokenize(tweet))).prob('pos')
    sentiments.insert(index,temp)
    



#Export sentiments.csv containing tweets and their predicted sentiments
combined = zip(ts,tweets,sentiments,userid,nb_followers)
df = DataFrame(data = combined, columns = ['ts','text','polarity','userid','nb_followers'])
df.to_csv('polarity.csv',index=False)
