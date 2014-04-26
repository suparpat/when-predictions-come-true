from pandas import DataFrame, read_csv
import train_subjectivity


#Read the tweets from the .csv file
df = read_csv("boeing.csv")
tweets = df.text #you can also use df['column_name']
ts = df.ts
userid = df.userid
nb_followers = df.nb_followers


#Train the Naive Bayes classifier with movie reviews corpus
train_subjectivity



#Get the predictions for the tweets using the trained classifier
subjectivity = []
ts2 = []
userid2 = []
nb_followers2 = []
count = tweets.count()
i = 0
for index,tweet in enumerate(tweets):
    #percent = float(index)/float(count)
    #print "{:4.2f}".format((percent)*100),"%"
    print '%d/%d' % (index, count)
    
    temp = train_subjectivity.classifier.prob_classify(train_subjectivity.word_feats(train_subjectivity.nltk.word_tokenize(tweet))).prob('sub')

    if temp>0.5:
        subjectivity.insert(i,temp)
        ts2.insert(i,ts[index])
        userid2.insert(i,userid[index])
        nb_followers2.insert(i,nb_followers[index])
        i = i + 1



#Export sentiments.csv
combined = zip(ts2,tweets,subjectivity,userid2,nb_followers2)
df = DataFrame(data = combined, columns = ['ts','text','subjectivity','userid','nb_followers'])
df.to_csv('subjectivity.csv',index=False)
