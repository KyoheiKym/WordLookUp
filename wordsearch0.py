
# coding: utf-8

# In[13]:


import time
import csv
import xml.etree.ElementTree as etree
import urllib2, sys
import re
import pandas as pd
hdr = {'User-Agent': 'Mozilla/5.0'}
data = pd.read_csv("tango.csv") #data install


# In[41]:

def func(arg1):
  site ="http://www.oxfordlearnersdictionaries.com/definition/english/" + arg1 + "_1?q=" + arg1
  req = urllib2.Request(site,headers=hdr)
  try:
    html = urllib2.urlopen(req).read()
  except urllib2.HTTPError as instance:
    if instance.code == 404:
        print arg1,"page doesn't exist"
        return pd.Series([arg1, "page does not exist"])
    else:
        print "can not access"
        return pd.Series([arg1, "cannot access"])
        ## アクセス制限された時の処理
  
  regularex = re.compile(r'<span class="def" id="' + arg1 + r'.*?>.*?</span>')
  re_compiled = re.compile(r'<.*?>')
  explanation = re.findall(regularex,html)
  #print explanation
  word_expl=[]
  word_expl.append(arg1)
  for n in explanation:
    word_expl.append(re_compiled.sub('',n))
    print "explanation",explanation
  return pd.Series(word_expl)


# In[42]:

def func1(data):
    return (pd.Series([data , data]))


# In[44]:

data["words"].apply(func)

data.to_csv('data.csv',index=False)


# In[ ]:




# In[ ]:



