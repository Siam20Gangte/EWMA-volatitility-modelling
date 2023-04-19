#!/usr/bin/env python
# coding: utf-8

# In[43]:


import pandas as pd
import numpy as np


# In[44]:


data = pd.read_csv("C:/Users/Siam/Desktop/ReInvent/Time series/Time series Ineuron/time-series-main/TSLA.CSV")


# In[45]:


data.head()


# In[107]:


df = data[["Date","Close"]]


# In[108]:


df = df.rename(columns={"Close":"NIFTY"})
df.head()


# In[109]:


df["ret"]= np.log(df["NIFTY"]/
                 df["NIFTY"].shift(1))
df= df.dropna()
df.head()


# ## EWMA formula
# ## sigma^2 = lambda*sigma^2 of t-1+(1-lambda)*mu^2 of t-1

# In[110]:


length = len(df["ret"])
length


# In[111]:


df.head()


# In[ ]:





# In[112]:


lamb = 0.94


# In[ ]:





# ## If latest observation is last then we use np.arange(length), but if its first then we use the below 

# In[113]:


series = np.arange(length-1,-1,-1)
series


# In[90]:


exp = np.power(lamb,series)*(1-lamb)


# In[114]:


## This was is neater
exp_1 = [(1-lamb)*lamb**i for i in series]
exp_1


# In[115]:


## Assign the series in the dataframe

df["exp"] = exp_1


# In[116]:


df.head()


# In[117]:


product = df["exp"]*df["ret"]**2
vol = np.sqrt(sum(product))**100
vol


# In[ ]:





# In[ ]:





# In[ ]:




