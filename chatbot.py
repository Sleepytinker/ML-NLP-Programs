import urllib.request
import os
import pandas as pd
import numpy as np
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')
tokenizer=RegexpTokenizer(r'\w+')
en_stopwords=set(stopwords.words('english'))
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib
from sklearn.model_selection import train_test_split
th= PorterStemmer()
data= pd.read_csv('https://cleveredailabs.s3.ap-south-1.amazonaws.com/amazon_alexa_6944.tsv',sep='\t')
def getStemmedReview(review):
  review=review.replace('<br /><br />', ' ')
  token = tokenizer.tokenize(review)
  new_tokens= [word for word in token if word not in en_stopwords]
  stemmed_tokens= [th.stem(var) for var in new_tokens]
  clean_review = ' '.join(stemmed_tokens)
  return clean_review

verified_reviews = data['verified_reviews'].apply(getStemmedReview)
x= data['verified_reviews']
y= data['feedback']
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)
we= TfidfVectorizer(sublinear_tf=True, encoding='utf-8',decode_error='ignore')
we.fit(x_train) 
x_train= we.transform(x_train)

x_test= we.transform(x_test)
model=LogisticRegression(solver='liblinear')
model.fit(x_train,y_train)

joblib.dump(model,'model.pkl')
joblib.dump(en_stopwords,'stopwords.pkl')
joblib.dump(we,'vectorizer.pkl')

 
loaded_model=joblib.load("model.pkl")
loaded_stop=joblib.load("stopwords.pkl")
loaded_vec=joblib.load("vectorizer.pkl")

def classify(text_box_1):
   X = loaded_vec.transform([text_box_1])
   y = loaded_model.predict(X)[0]
   proba = np.max(loaded_model.predict_proba(X))
   if proba > 0.90:
       return'positive'
   else:
      return'negative'

print(X[0])

ch= 'yes'
while ch=='yes':
  func= input('write any review')

  if classify(func)=='positive':
    print('Thankyou for the wonderful review')
  else:
    improve= input('Kindly suggest areas for improvement')
    print('thankyou for the feedback!')


  ch= input('do you wish to provide another review? yes/no')

print('thankyou for the feedback')
