#!/usr/bin/env python
# coding: utf-8

# # Cryptocurrency prices
# 
# * **Filename:**  `cryptocurrencies.csv`
# * **Description:** Cryptocurrency prices for a handful of coins over time.
# * **Source:** https://coinmarketcap.com/all/views/all/ but from a million years ago (I cut and pasted, honestly)
# 
# ### Make a chart of bitcoin's high, on a weekly basis
# 
# You might want to do the cherry blossoms homework first, or at least read the part about `format=` and `pd.to_datetime`.
# 
# *Yes, that's the entire assignment. It isn't an exciting dataset, but it's just dirty enough to make charting this a useful experience.*

# In[1]:


import pandas as pd 

df = pd.read_csv('cryptocurrencies.csv')


# In[2]:


df


# In[3]:


df.dtypes


# In[4]:


df.replace(',','', regex=True, inplace=True)


# In[5]:


df


# In[6]:


df.coin.value_counts()


# In[29]:


df_bitcoin = df.iloc[:365]


# In[36]:


df_bitcoin['date'] = pd.to_datetime(df_bitcoin.date, format='%d-%b-%y', errors = 'coerce').dropna()
df_bitcoin.date


# In[37]:


# I don't know why this won't work and I give up. 


# In[39]:


df_bitcoin["week"]= df_bitcoin.date.dt.strftime("%W")


# In[40]:


df_bitcoin['high'] = df_bitcoin['high'].astype(float)


# In[41]:


df_bitcoin.dtypes


# In[48]:


df_bitcoin.groupby('week').high.sum().plot(figsize = (20, 10))


# In[47]:


df_bitcoin.high.plot(x = 'date', y= 'high', figsize = (20, 10))


# In[127]:


df_bitcoin.plot


# In[ ]:





# In[ ]:




