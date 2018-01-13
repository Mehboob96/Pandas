#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 10:42:54 2018

@author: codept
"""

import pandas as pd
import pandas_datareader.data as web
import datetime as dt

country_data = {
        'country' : ['India','USA','Pakistan','Iraq','England','SouthAfrica'],
        'population' : [1.3,1.4,0.5,0.3,1.1,0.8]
    }

country_data

df = pd.DataFrame(country_data)
type(df)

type(df['country'])
df['capital'] = ['Delhi','NewYork','Lahore','Xyz','London','CapeTown']

df[['country','capital','population']]
"""df['money','PM'] = [[100000,500000,800000,4000,50000,60000],['Modi','Trump','Majid','Sam','Luis','Faf']]"""
df['money'] = [100000,500000,800000,4000,50000,60000]
df['PM'] = ['Modi','Trump','Majid','Sam','Luis','Faf']

df['XYZ'] = df['population'] + df['money']
df['XYZ']

df.loc('country')

"""
to set 1st column as SerialNo
"""

df.set_index('country',inplace=True)

df.loc['India']

df.iloc[5]
"""inplace is very important for doing pemanent changes if we dont use implace it will not take any action in main dataframe
by default it is false
"""

"""To Delete    Axis 0 is Row Axis 1 is Column"""

df.drop('XYZ',axis=1)
df
df.drop('XYZ',axis=1,inplace=True)

df['money'] > 50000

df[df['money'] > 5000][['capital','PM','money']]
df['money']

df[(df['population'] < 1.2) & (df['money'] > 50000)].iloc[0]['capital']

start = dt.datetime(2010,1,1)
end = dt.datetime(2017,12,27)

df = web.DataReader("F","yahoo",start,end)