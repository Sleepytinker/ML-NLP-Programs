#import libraries
import requests
from bs4 import  BeautifulSoup

URL = 'https://www.flipkart.com/air-conditioners/pr?sid=j9e,abm,c54&p[]=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&p[]=facets.technology%255B%255D%3DInverter&p[]=facets.serviceability%5B%5D%3Dtrue&otracker=categorytree&otracker=nmenu_sub_TVs%20%26%20Appliances_0_Inverter%20AC'

#get requests
page = requests.get(URL)


#make soup
soup = BeautifulSoup(page.content, 'html.parser')


#make two lists
products= []
prices= []

#Find container class and iterate into it and finally append all data  in their respective lists.

for a in soup.findAll('a',href=True, attrs={'class':'_1fQZEK'}):
  name=a.find('div', attrs={'class':'_4rR01T'})
  price=a.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
  products.append(name.text)
  prices.append(price.text.encode('ascii', 'ignore').decode('ascii'))

#import pandas
import pandas as pd

#store in dataframe
df = pd.DataFrame({'Product Name':products,'Price':prices}) 

#print top 6 rows of df dataframe.
print(df.head(6))
