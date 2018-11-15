import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
import operator
import json
import re, pprint
from collections import Counter
import os
import requests
import urllib
import io
from watson_developer_cloud import AlchemyLanguageV1
from alchemyapi import AlchemyAPI
alchemyapi = AlchemyAPI()
alchemy_language = AlchemyLanguageV1(api_key = '474b0259ddb86806480495a18bd58d4abaf9f0ec')

#import mysql.connector
punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt', 'via']
os.chdir(r'C:\Users\sudishrestha\Desktop\september 8')
#accesing the saved tweets
fname = io.open('streams.txt', encoding ='latin2')
#count_all = Counter()
for line in fname:
    tweet = json.dumps(line)
    tweet_storage =  json.loads(tweet)
    response = alchemyapi.sentiment("text", line)
    status = response.get('status')
    if status == 'ERROR':
        print(response['statusInfo'])
    else:
        print "Sentiment: ", response["docSentiment"]["type"]
        json_data = alchemy_language.keywords(text= line, sentiment= 0)
        print (json_data)
        print(json.dumps(json_data, indent=2))
        with open('streamser.txt', 'a') as the_file:
            the_file.write("Sentiment: " + response["docSentiment"]["type"] + json.dumps(json_data, indent=2) + "\n tetetetetetetetetet" +"\n")

