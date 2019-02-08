#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 09:58:01 2019

@author: SydMacBook
"""

import pandas as pd
import numpy as np

data = pd.read_csv('../data/38650-password-sktorrent.txt', header=None)

import re

data.columns = ['original']
    
data['original'] = data['original'].astype(str)

data["specialcharsplit"] = ""
data["extrawordsplit"] = ""

import wordsegment as ws

from wordsegment import load, segment

load()
  
def flat(l):
    for k in l:
        if not isinstance(k, (list, tuple)):
            yield k
        else:
            yield from flat(k)
  
for index, row in data.iterrows():
  row['specialcharsplit'] = re.findall(r'[0-9]+|[a-zA-Z]+|[^a-zA-Z0-9]+',row['original'])
  passwdstring=[]
  for i in row['specialcharsplit']:
     templist = segment(i)
     if(templist):
       passwdstring.append(templist)
     else:
       passwdstring.append(i)
  row['extrawordsplit'] = list(flat(passwdstring))
  
  
funlist = ['i', 'am', 'a', 'list']

funstring = ""

for indexx, vall in enumerate(funlist):
    funstring = funstring + funlist[indexx]
    
data["iscapital"] = ""

for index, row in data.iterrows():
    array = []
    for c in row['original']:
      array.append(c.isupper() + 0)
    row["iscapital"] = array

length = 0
for indexx, vall in enumerate(data.iloc[0]['extrawordsplit']):
    for i in range(0, len(vall)-1):
        if (data.iloc[0]['iscapital'])[length + i] == 1:
            ((data.iloc[0]['extrawordsplit'])[indexx][i]).upper()
    length = length + len(vall)

import nltk
from nltk.corpus import stopwords
set(stopwords.words('english'))