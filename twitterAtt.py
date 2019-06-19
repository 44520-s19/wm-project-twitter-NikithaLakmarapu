# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 16:43:38 2019

@author: S534690
"""

import pickle
with open('trump.pkl','rb') as f:
    donald_tweets=pickle.load(f)
for i in range(len(donald_tweets)):
    print(donald_tweets[i].retweet_count)
    print(len(donald_tweets[i].text.split()))
    
