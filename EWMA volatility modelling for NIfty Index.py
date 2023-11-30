#!/usr/bin/env python
# coding: utf-8



import pandas as pd
import numpy as np


data = pd.read_csv("C:/Users/Siam/Desktop/ReInvent/Time series/Time series Ineuron/time-series-main/TSLA.CSV")


data.head()


df = data[["Date","Close"]]


df = df.rename(columns={"Close":"NIFTY"})
df.head()


df["ret"]= np.log(df["NIFTY"]/
                 df["NIFTY"].shift(1))
df= df.dropna()
df.head()


## EWMA formula
## sigma^2 = lambda*sigma^2 of t-1+(1-lambda)*mu^2 of t-1



length = len(df["ret"])
length

df.head()

lamb = 0.94



# ## If latest observation is last then we use np.arange(length), but if its first then we use the below 

series = np.arange(length-1,-1,-1)
series


exp = np.power(lamb,series)*(1-lamb)


## This was is neater
exp_1 = [(1-lamb)*lamb**i for i in series]
exp_1

## Assign the series in the dataframe

df["exp"] = exp_1



df.head()


product = df["exp"]*df["ret"]**2
vol = np.sqrt(sum(product))**100
vol




