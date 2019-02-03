#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 09:58:01 2019

@author: SydMacBook
"""

import pandas as pd
import numpy as np

data = pd.read_csv('data/38650-password-sktorrent.txt', header=None)

s = "string"

s_list = list(s)

data["split"] = ""

data.columns = ['original', 'split']

for index, row in data.iterrows():
    row['split'] = list(row['original'])


