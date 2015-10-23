
# coding: utf-8

# In[11]:


import time
import csv
import xml.etree.ElementTree as etree
import urllib2, sys
import re
import pandas as pd
import numpy as np
hdr = {'User-Agent': 'Mozilla/5.0'}
data = pd.read_csv("data.csv") #data install


# In[12]:

def func(arg1):
    site ="http://www.oxfordlearnersdictionaries.com/definition/english/" + arg1 + "_1?q=" + arg1
    req = urllib2.Request(site,headers=hdr)
    try:
        html = urllib2.urlopen(req).read()
    except urllib2.HTTPError as instance:
        if instance.code == 404:
            #print arg1,"page doesn't exist"
            return pd.Series([arg1, "page does not exist"])
        else:
            #print "can not access"
            return pd.Series([arg1, "cannot access"])
        
    regularex = re.compile(r'<span class="def" id="' + arg1 + r'.*?>.*?</span>')
    re_compiled = re.compile(r'<.*?>')
    explanation = re.findall(regularex,html)
    #print explanation
    word_expl=[]
    word_expl.append(arg1)
    index1=["data"]
    index1.append("1")
    for i in range(len(explanation)-1):
        index1.append(str(i+1))
    for n in explanation: 
        word_expl.append(re_compiled.sub('',n))
        #print "explanation",explanation

    return pd.Series(word_expl)


# In[13]:

data = data["word"].apply(func)

columname=[]
for i in range(len(data.columns)):
    if i ==0:columname.append("word")
    else: columname.append("definition_"+str(i))
data.columns = columname

data.to_csv('data.csv',index=False,header=True)


# In[14]:

data


# In[ ]:



