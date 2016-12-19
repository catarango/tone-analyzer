
# coding: utf-8

# In[122]:

import urllib.request
URL = 'https://www.washingtonpost.com/news/the-fix/wp/2016/10/19/the-final-trump-clinton-debate-transcript-annotated/'

def getWebpage(theURL):
    response = urllib.request.urlopen(theURL)
    html = response.read()
    html = html.decode()
    print("got it!")
    f = open('debatetext.txt', 'w')
    f.write(html)
    f.close()
    print("all done!")    
    
getWebpage(URL) 

#use regular expressions to parse out clinton and trump text and join them into one string
import re
data = open(r'debatetext.txt','r').read()
print(len(data))
clinton = re.findall(r'(?<=CLINTON:)(.*)(?=</p>)', data, re.MULTILINE)
trump = re.findall(r'(?<=TRUMP:)(.*)(?=</p>)', data, re.MULTILINE)
clinton = [''.join(clinton[0:len(clinton)])]
trump = [''.join(trump[0:len(trump)])]
print(len(clinton), len(trump))

#use the Watson API to analyze tone of both candidates
import json
from watson_developer_cloud import ToneAnalyzerV3
tone_analyzer = ToneAnalyzerV3(
   username='5ad91819-3a78-41d2-beee-71ffda65c6e2',
   password='VLaps78fvlQ3',
   version='2016-05-19')

#retrieve, parse clinton data + push to file
clinton = json.dumps(tone_analyzer.tone(text= clinton[0]), indent=2)
clinton_parsed = (json.loads(clinton)['document_tone']) #just keeps document tone, no sentences
for x in clinton_parsed['tone_categories']:
    for y in x['tones']:
        print(y['tone_name'], y['score'])
        tone= ((y['tone_name'],',', str(y['score'])))
        f = open('clintontone.csv','a')
        f.write((''.join(tone))+'\n')
        f.close()
#retrieve, parse trump data + push to file        
trump = json.dumps(tone_analyzer.tone(text= trump[0]), indent=2)
trump_parsed = (json.loads(trump)['document_tone']) #just keeps document tone, no sentences
for x in trump_parsed['tone_categories']:
    for y in x['tones']:
        print(y['tone_name'], y['score'])
        tone= ((y['tone_name'],',', str(y['score'])))
        f = open('trumptone.csv','a')
        f.write((''.join(tone))+'\n')
        f.close()           


