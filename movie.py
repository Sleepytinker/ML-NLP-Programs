import pandas as pd
import nltk
import re
nltk.download('punkt')
nltk.download('stopwords')
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
data= pd.read_csv('https://cleveredailabs.s3.ap-south-1.amazonaws.com/train_1_9933.tsv', sep='\t')


#print top 5 rows
print(data.head(5))

#print number of row and column
print(data.shape)

#print data type of each column
print(data.dtypes)

#print all general info about each column
print(data.info())

#Count of each unique value in Sentiment column
print(data['Sentiment'].unique())

ps = PorterStemmer()

#write your code here
msg = []

for i in range(0, data.shape[0]):
    review = re.sub('[^a-zA-Z]', ' ', data['Phrase'][i])
    review = review.lower()
    review = review.split()
    review = [ps.stem(word) for word in review if not word in stopwords.words('english')]
    review = ' '.join(review)
    msg.append(review)

#print list msg
print(msg)

#import library
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer

#load the module
cv = TfidfVectorizer()

#Fit with msg data
X = cv.fit_transform(msg).toarray()

#Create variable Y
Y=np.array(data['Sentiment'])

#print dependent variable X
print(X)

print()
#print the independent variable Y
print(Y)
