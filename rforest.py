#write your code here
import pandas as pd
import numpy as np
import nltk
import re
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

data= pd.read_csv('https://cleveredailabs.s3.ap-south-1.amazonaws.com/train_1_9933.tsv', sep='\t')
msg=[]

lemmatizer=WordNetLemmatizer()
for i in range(0,data.shape[0]):
    review= re.sub('[^a-zA-Z]', ' ', data['Phrase'][i])
    review=review.lower()
    review= review.split()

    review = [lemmatizer.lemmatize(word) for word in review if not word in stopwords.words('english')]
    review= ' '.join(review)
    msg.append(review)
print(msg)
cv=TfidfVectorizer(max_features=3000)
X= cv.fit_transform(msg).toarray()

Y= np.array(data['Sentiment'])
x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.2,random_state=42)
from sklearn.ensemble import RandomForestClassifier

#Load library
rfc = RandomForestClassifier(n_estimators=100,criterion='gini',random_state=42)

#Fit the model
rfc.fit(x_train,y_train)

#predict x_test data
pred = rfc.predict(x_test)

#print predicted output
print(pred)

#Evaluate the accuracy of model
from sklearn.metrics import accuracy_score
auc = accuracy_score(y_test,pred)

#print accuracy
print(auc)

#######################################################################

