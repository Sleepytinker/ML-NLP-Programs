#import library
import urllib.request
import nltk
import string
nltk.download('punkt')
nltk.download('popular', quiet=True)
nltk.download('wordnet') 
import warnings
warnings.filterwarnings('ignore')
from nltk.stem import WordNetLemmatizer
import random 
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

url = "https://cleveredailabs.s3.ap-south-1.amazonaws.com/chatbot_9606.txt"

#Open the given url to read text from it
file = urllib.request.urlopen(url)

#Remove '#' before below line to see file data and put again '#' symbol.
print(file.read())

raw=file.read().decode("utf-8") 


#convert into lowercase
raw=raw.lower()

#convert into group of sentences
sent_tokens = nltk.sent_tokenize(str(raw)) 

#convert into group of words
word_tokens = nltk.word_tokenize(str(raw))

#Load the Lemmatizer
lemmer = WordNetLemmatizer()

#Define LemTokens function
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

#Define remove_punctuation function
def remove_punctuation(text):
        tokens = nltk.word_tokenize(text)
        words = [w.lower() for w in tokens if w.isalnum()]
        return LemTokens(words)

#Call and print function
print(remove_punctuation("what has happened to you?"))


GREETING_INPUTS = ["hello", "hi", "greetings", "sup", "what's up","hey"]
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]

#Define greeting function with one argument sentence
def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)
          
#Call and print the output of greeting function
print(greeting('hello'))


#Define response function and convert text into number then use cosine similarity function to compare documents and finally return second highest cosine similarity index value.

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#Define response function and convert text into number then use cosine similarity function to compare documents and finally return second highest cosine similarity index value.

def response(user_response):
  robo_response=''
  sent_tokens.append(user_response)
  TfidfVec = TfidfVectorizer(tokenizer=remove_punctuation, stop_words='english')
  tfidf = TfidfVec.fit_transform(sent_tokens)
  value = cosine_similarity(tfidf[-1], tfidf)
  idx=value.argsort()
  flat = value.flatten()
  flat.sort()
  print(flat)
  req_tfidf = flat[0]
  print(req_tfidf)
  if (req_tfidf==0):
    robo_response=robo_response+"I am sorry! I don't understand you"
    return robo_response
  else:
      robo_response = robo_response+sent_tokens[idx]
      return robo_response


print("BOT: My name is BOT. I will answer your queries about Chatbots.")
user_response = ["Hi","what is chatbot application","what is an AI","Where chatbots are used", "chatbot design","What is Turing Test" ,"Thank you",'Bye']

#Now check few greeting questions like bye, thank you and other query response.

for user_response in user_response:
  user_response=user_response.lower()
  if (user_response!='bye'):
    if (user_response=='thanks' or user_response=='thank you' ):
      print("User:" + user_response)
      print("BOT: You are welcome..")
    else:
      if (greeting(user_response)!=None):
        print("User:" + user_response)
        print("BOT: "+greeting(user_response))
      else:
        print("User:" + user_response)
        print("BOT: ",end="")
        print(response(user_response))
        sent_tokens.remove(user_response)
  else:
    print("User:" + user_response)
    print("BOT: Bye! take care..")
    
  ############################################################################################
  import urllib.request

url = "https://cleveredailabs.s3.ap-south-1.amazonaws.com/chatbot_9606.txt"

#Open the given url to read text from it
file = urllib.request.urlopen(url)

#Remove '#' before below line to see file data and put again '#' symbol.
#print(file.read())

raw=file.read().decode("utf-8") 
import nltk
import string
nltk.download('punkt')
nltk.download('popular', quiet=True)
nltk.download('wordnet') 
import warnings
warnings.filterwarnings('ignore')
from nltk.stem import WordNetLemmatizer

#convert into lowercase
raw=raw.lower()

#convert into group of sentences
sent_tokens = nltk.sent_tokenize(str(raw)) 

#convert into group of words
word_tokens = nltk.word_tokenize(str(raw))

#Load the Lemmatizer
lemmer = WordNetLemmatizer()

#Define LemTokens function
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

#Define remove_punctuation function
def remove_punctuation(text):
        tokens = nltk.word_tokenize(text)
        words = [w.lower() for w in tokens if w.isalnum()]
        return LemTokens(words)

#Call and print function
print(remove_punctuation("what has happened to you?"))
import random 
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def response(user_response):
    robo_response=''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=remove_punctuation, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    value = cosine_similarity(tfidf[-1], tfidf)
    idx=value.argsort()[0][-2]
    flat = value.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        robo_response=robo_response+"I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = robo_response+sent_tokens[idx]
        return robo_response

print("BOT: My name is Robo. I will answer your queries about Chatbots.")
user_response = ["Hi","what is chatbot application","what is an AI","Where chatbots are used", "chatbot design","What is Turing Test" ,"Thank you",'Bye']
for user_response in user_response:
   user_response=user_response.lower()
   if(user_response!='bye'):
       if(user_response=='thanks' or user_response=='thank you' ):
         print("User:" + user_response)
         print("BOT: You are welcome..")
       else:
            print("User:" + user_response)
            print("BOT: ",end="")
            print(response(user_response))
   else:
      print("User:" + user_response)
      print("BOT: Bye! take care..")
      
      
      
      ####################################################################################
      
      import urllib.request
import nltk
import string
nltk.download('punkt')
nltk.download('popular', quiet=True)
nltk.download('wordnet') 
import warnings
warnings.filterwarnings('ignore')
from nltk.stem import WordNetLemmatizer
import random 
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

url= 'https://cleveredailabs.s3.ap-south-1.amazonaws.com/india_192.txt'
file = urllib.request.urlopen(url)
#Remove '#' before below line to see file data and put again '#' symbol.
#print(file.read())

raw=file.read().decode("utf-8") 
#convert into lowercase
raw=raw.lower()

#convert into group of sentences
sent_tokens = nltk.sent_tokenize(str(raw)) 

#convert into group of words
word_tokens = nltk.word_tokenize(str(raw))

#Load the Lemmatizer
lemmer = WordNetLemmatizer()

#Define LemTokens function
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

def remove_punctuation(text):
        tokens = nltk.word_tokenize(text)
        words = [w.lower() for w in tokens if w.isalnum()]
        return LemTokens(words)

print(remove_punctuation('hello, how are you'))

GREETING_INPUTS = ["hello", "hi", "greetings", "sup", "what's up","hey"]
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]

#Define greeting function with one argument sentence
def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)
          
#Call and print the output of greeting function
print(greeting('hello'))

def response(user_response):
    robo_response=''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=remove_punctuation, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    value = cosine_similarity(tfidf[-1], tfidf)
    idx=value.argsort()[0][-2]
    flat = value.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        robo_response=robo_response+"I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = robo_response+sent_tokens[idx]
        return robo_response
        
print("BOT: My name is Robo. I will answer your queries about India.")
user_response = ["Hi","what is the History of India","Tell me about Politics and government in India","What are the Economic relations of India", "Cultures in India","What is the Education system in India" ,"Thank you",'Bye']
for user_response in user_response:
   user_response=user_response.lower()
   if (user_response!='bye'):
      if (user_response=='thanks' or user_response=='thank you' ):
        print("User:" + user_response)
        print("BOT: You are welcome..")
      else:
        if (greeting(user_response)!=None):
          print("User:" + user_response)
          print("BOT: "+greeting(user_response))
        else:
          print("User:" + user_response)
          print("BOT: ",end="")
          print(response(user_response))
          sent_tokens.remove(user_response)
   else:
      print("User:" + user_response)
      print("BOT: Bye! take care..")
    
