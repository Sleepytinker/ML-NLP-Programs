# NLTK-NLP-Programs

It is a collection of programs, independant from each other, that was built using Natural Language Processing (NLP), and Machine Learning models.

Few programs (webscrapping.py, searchbot.py) employ webscrapping to search user-defined query and display information gathered from sites including Amazon, Flipkart, Wikipedia.

Programs like bog.py and lemmatize.py focus mainly scrapping user posts across social media to extract information that seeks to locate and classify named entites in text such as the names of persons, organizations, locations etc. Using POS tagging and Named Entity Recognition,  meaningful phrases from unstructured text is extracted and classified.

In movie.py the dataset extracted from movie reviews is first cleaned to remove slang and stop words, the text is then tokenized by splitting data into pairs of sentences and words before performing lemmatization to evaluate sentence-context and convert words to their meaningful base forms. Finally, emotions are extraced from the refined text and classified as happiness, frustration, anger, sadness, and so on.

rforest.py as the name suggests using random forest techniques, with TF-IDF (term frequency- inverse document frequency) to perform search operations and data retrieval in the documents. The documents are first mined for information (text-minning), the text extracted is summarized and transformed to obtain desired results. It basically functions as a twitted sentiment analyzer.

chatbot.py uses Fine-grained Sentiment Analysis (polarity precision) to classify (very positively, Positive, Neutral, Negative, very negative) and analyze a dataset of most of the diffrent types of user reviews found on Amazon. It then uses a Machine-learning based approach (after training the dataset) to classify and gauge newer user reviews/feedbacks. It predicts if the review is negative/neutral and asks for suggested areas of improvement and if the review is positive, thanks the user.

# Libraries Used

* Pandas <br />
* Numpy <br />
* NLTK (from nltk.tokenize import RegexpTokenizer, from nltk.stem.porter import PorterStemmer, from nltk.corpus import stopwords)<br />
* Urllib <br />
* Sklearn (from sklearn.feature_extraction.text  import TfidfVectorizer) <br />
* Bs4 <br />
* NRCLex <br />
* Requests <br />




