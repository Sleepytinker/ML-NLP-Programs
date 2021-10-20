#import library
import pandas as pd

#Read review.csv file
data=pd.read_csv('reviews_9120.csv')

#print top5 rows
print(data.head(5))

#print number of row and column
print(data.shape)

#print datatypes of each column
print(data.dtypes)

#Store all stop words
word_stop=["is","are","so","a","in","up","the","as","it","I","the","did","an","You","it's","of","from","my","your"]

#Clean text
data["clean_text"]=data['Tweets'].apply(lambda x: ' '.join([word for word in x.split() if word not in word_stop]))

#print top 5 rows
print(data.head(5))

#import all library
import vaderSentiment
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#Load library
analyser = SentimentIntensityAnalyzer()

#Apply polarity scores on clean_text
data['scores'] = data['clean_text'].apply(lambda review: analyser.polarity_scores(review))

#print top 5 rows of data
print(data.head(5))

#import library
import textblob
#calculate sentiment polarity on clean_text
data['polarity'] = data['clean_text'].apply(lambda review: textblob.TextBlob(review).sentiment.polarity)

#print top 5 rows
print(data.head(5))


##########################################################################
import textblob
from nrclex import NRCLex
import vaderSentiment
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser= SentimentIntensityAnalyzer()
tweet1 = "The curry was bad, however pasta was delicious"
tweet2 = "The curry was ok and pasta was delicious"
print(NRCLex(tweet1).top_emotions)
print(NRCLex(tweet2).top_emotions)
print(analyser.polarity_scores(tweet1))
print(analyser.polarity_scores(tweet2))
print(textblob.TextBlob(tweet1).sentiment.polarity)
print(textblob.TextBlob(tweet2).sentiment.polarity)

##########################################################################

from nrclex import NRCLex 
#Define a new function emotion.
def emotion(x):
  text=NRCLex(x)
  if text.top_emotions[0][1] == 0.0:
    return "No emotion"
  else:
    return text.top_emotions[0][0]

#Store emotion in Emotion column
data['Emotion'] = data['text'].apply(emotion)

#print top 5 rows
print(data.head(5))
