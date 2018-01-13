#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 13:59:26 2018

@author: codept
"""

import pandas as pd
import numpy as np

data = {
        'A' : [1,2,np.nan],
        'B' : [5,np.nan,2],
        'C' : [1,2,3]
         }

data
df = pd.DataFrame(data)

df.dropna(axis=1)
df.fillna(df.min(),axis=0)


import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')
plt.plot(df['High'])
plt.show()


df = pd.read_csv("Documents/Work/indiacencesdata.csv")

df.set_index('Year',inplace=True)
plt.plot(df['Population'])
plt.show()


df = pd.read_csv("Documents/Work/Salaries.csv")
df.set_index('Id',inplace=True)
plt.plot(df['Agency'])
plt.show()

"""df.iloc[df['BasePay'].min()]
"""

df[df['EmployeeName'] == 'NATHANIEL FORD'][['EmployeeName','TotalPay']]


df[df['TotalPayBenefits'] == df['TotalPayBenefits'].min()][['EmployeeName']]

sum(df[df['Year'] == 2013]['JobTitle'].value_counts() == 1 )

dat = pd.read_csv("Documents/Work/Ecommerce Purchases.csv")
dat.info()
dat[dat['Language'] == 'en']['Language'].count()

dat['Job'].value_counts().head(5)

dat[dat['Lot'] == '90 WT']['Purchase Price']

dat[dat['Credit Card'] == 4926535242672853]['Email']
dat[(dat['Purchase Price'] > 95) & (dat['CC Provider'] == 'American Express')]['Purchase Price'].count()