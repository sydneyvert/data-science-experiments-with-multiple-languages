#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 09:58:01 2019

@author: SydMacBook
"""

import pandas as pd
import numpy as np

data = pd.read_csv('~/Documents/DS\ Projects/Project\ 3/data-science-toolbox-kate-syd-jun/data/38650-password-sktorrent.txt', header=None)

s = "string"

s_list = list(s)

data["split"] = ""

data.columns = ['original', 'split']

for index, row in data.iterrows():
    row['split'] = list(row['original'])

import re

s2 ='letter123num45***'

s2_split = re.split('(\d+)',s2)

data["numletsplit"] = ""

for index, row in data.iterrows():
    row['numletsplit'] = re.split('(\d+)', row['original'])
    
import wordsegment as ws

from wordsegment import load, segment

seg = 'testmysplitsegmentpleaseandthankyou'

load()
segtry = segment(seg)

#works for individual words in lists:
segtry = segment((data.iloc[1]['numletsplit'])[0])

new_list = list()
for i, val in enumerate(data.iloc[53]['numletsplit']):
    new_list.append(segment((data.iloc[53]['numletsplit'])[i]))

data["extrawordsplit"] = ""

for index, row in data.iterrows():
    row['extrawordsplit'] = list()
    for ind, val in enumerate(row['numletsplit']):
        row['extrawordsplit'].append(segment((row['numletsplit'])[ind]))
