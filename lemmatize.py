import pandas as pd
import nltk
import re
nltk.download('punkt')
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer

data=pd.read_excel('https://cleveredailabs.s3.ap-south-1.amazonaws.com/train_data_6833.xlsx')

#print top 5 rows
print(data.head(5))
word_stop=["is","are","so","a","in","up","the","as","it","I","the","did","an","You","it's","of","from","my","your"]

#Create function

def clean_tweet(tweet):
   tweet=tweet.lower()
   wordnet_lemmatizer = WordNetLemmatizer()
   tweet=' '.join(re.sub('[^a-zA-Z]'," ",tweet).split())
   tweet = nltk.word_tokenize(tweet)
   tweet = " ".join([wordnet_lemmatizer.lemmatize(word) for word in tweet if not word in word_stop])
   return tweet

#create new column called clean_tweet
data['clean_tweet']=data['text'].apply(clean_tweet)

#print top 5 rows
print(data.head(5))

print(data['text'][2])
