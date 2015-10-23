# -*- coding:utf-8 -*-
import time
import csv
import feedparser
import xml.etree.ElementTree as etree
import urllib2, sys
import re
hdr = {'User-Agent': 'Mozilla/5.0'}

def func(arg1):
  site ="http://www.oxfordlearnersdictionaries.com/definition/english/" + arg1
  req = urllib2.Request(site,headers=hdr)
  la =[]
  try:
    #print "site",site
    html = urllib2.urlopen(req).read()
  except urllib2.HTTPError as instance:
    if instance.code == 404:
        print arg1,"page doesn't exist"
        la.append(arg1)
        return la
    else:
        print "can not access"
        la.append(arg1)
        return la
        ## アクセス制限された時の処理
  seiki = re.compile(r'<span class="d" id="' + arg1 + r'.*?>.*?</span>')
  p = re.compile(r'<.*?>')
  listk = re.findall(seiki,html)
  la.append(arg1)
  d = 0
  for n in listk:
    laaa = p.sub('',n)
    print "laaa",laaa
    la.append(laaa)
    #print d+1,la
    d = d + 1
  return la

r = open('data.csv', 'rb')
dataReader = csv.reader(r)
data =[]
rr = re.compile(r'\t.*?\t')
for row in dataReader:
#  print "row",row
#  print "row0", row[0]
#  print "row1",row[1]
  #m = rr.search(row[0])
  #print "m",m
  try:
    #mm = m.group(0)
    #print "mm",mm
    if row[1] < 1 or row[1] ==None:
      t = re.compile(r'\t')
      u = t.sub('',row[0])
      uu = func(u)
      data.append(uu)    # data = rows of csv
    #print uu 
    else:
      data.append(row)

  except:
    t = re.compile(r'\t')
    u = t.sub('',row[0])
    uu=func(u)
    data.append(uu)
    continue

f = open('data.csv', 'ab')
print "data",data
csvWriter = csv.writer(f)
wordlist =[]
csvWriter.writerows(data)
#print "data" , data
#print "wordlist",wordlist
f.close()
