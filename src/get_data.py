# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 16:29:50 2019

@author: 43739
"""

import pandas as pd
import numpy as np
import os
df=pd.read_csv("D:/database.csv")

data=pd.DataFrame(df)
data.describe()
data4use=data.drop(['issuer', 'optionid','cp_flag','exercise_style','index_flag','delta','gamma','best_bid','best_offer'], axis=1)
data4use["exdate"]=pd.to_datetime(data4use["exdate"])
data4use["date"]=pd.to_datetime(data4use["date"])
data4use["price"]=(data['best_bid']+data['best_offer'])/2
data4use["T"]=data4use["exdate"]-data4use["date"]
data4use["T"]=data4use["T"]/np.timedelta64(1,'D')
data4use["strike_price"]=data4use["strike_price"]/1000

data4output=data4use.loc[(data4use['T'] <=100)&(data4use['T'] >=30)]

os.chdir("D:/")
data4output.to_csv('data4output.csv')

