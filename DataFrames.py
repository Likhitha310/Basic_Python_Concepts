#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


data1 = np.random.randn(10,3)
data2 = np.random.randn(7,3)


# In[3]:


df1 = pd.DataFrame(data1, columns=["Col1", "Col2", "Col3"])
df2 = pd.DataFrame(data2, columns=["Col1", "Col2", "Col3"])


# In[4]:


df1


# In[5]:


df2


# In[26]:


df3 = pd.concat([df1,df2], ignore_index=True)


# In[27]:


df3


# In[28]:


for i in df3.Col3:
  print(i)


# * iteritems

# In[29]:


# For columns
for key,value in df3.iteritems():
  print(key,value)


# # * iterrows()

# In[30]:


# For rows
for index,row in df3.iterrows():
  print(index, row)


# # * Sort - sort_index()

# In[31]:


unsorted_df = pd.DataFrame(np.random.randn(10,3), 
                           index = [5,7,3,9,2,1,9,11,21,4],
                           columns = ['Col1', 'Col2', 'Col3'])


# In[32]:


unsorted_df


# In[33]:


unsorted_df.sort_index()


# In[34]:


unsorted_df.sort_index(ascending=False)


# In[35]:


unsorted_df.sort_index(axis=1)


# In[36]:


unsorted_df.sort_index(axis=1, ascending=False)


# # * sort_values()

# In[37]:


df = pd.DataFrame({"Apples":[50,95, 105,75],"Grapes":[110,45,99,0]})


# In[38]:


df


# In[39]:


df.sort_values(by=['Apples', 'Grapes'])


# In[40]:


df.sort_values(by=['Apples', 'Grapes'],kind='mergesort')


# * Stats - Advanced

# In[41]:


df3


# In[42]:


df3


# # Data Cleaning

# In[45]:


df = pd.DataFrame(np.random.randn(5,3),
                  index = ["A", "C", "E", "F", "G"],
                  columns = ["Col1", "Col2", "Col3"])


# In[46]:


df


# In[47]:


df = df.reindex(["A", "B", "C", "D", "E", "F", "G", "H"])


# In[48]:


df


# # * isnull()

# In[49]:


df.isnull()


# In[50]:


df.isnull().sum()


# In[51]:


df.isnull().sum().sum()


# In[52]:


df['Col1'].isnull()


# In[53]:


df.loc["G"].isnull()


# # * isna()

# In[54]:


df.isna()


# In[55]:


df.isna().dtypes


# In[56]:


df.dtypes


# # * notnull()

# In[57]:


df.notnull()


# In[58]:


df.notnull().sum(1)


# In[59]:


df.count()


# # * Clean Missing (NaN) Values

# In[60]:


df


# # * fillna()

# In[61]:


df.fillna(10)


# In[63]:


df


# In[64]:


df.fillna(method='pad')


# In[65]:


df.fillna(method='pad',axis=1)


# In[66]:


df.fillna(method='bfill')


# # * dropna()

# In[67]:


df.dropna(axis=1)


# # * Replacing values - replace()

# In[68]:


df


# In[69]:


df.replace({1.046703:100.0, 2.479047:200.0})


# In[70]:


df.replace({50:90, 99:245})


# In[71]:


df


# In[72]:


df.Apples.loc[2] = 500


# In[73]:


df


# In[74]:


df.Grapes.loc[2] = 299
df.loc[____, ___]


# In[75]:


df


# In[76]:


df.Apples.loc[3] = 50


# In[77]:


df


# # Handle Duplicates Values

# In[78]:


df.duplicated(subset=['Apples'])


# In[79]:


df


# In[80]:


df.drop_duplicates(subset=['Apples'])


# # Import/Export a dataset

# In[81]:


data = "stocks.csv"
df = pd.read_csv(data)


# In[82]:


df


# In[83]:


df.to_csv("file.csv")


# In[84]:


df['Open'].nunique()


# In[85]:


df.info()


# In[87]:


df = pd.read_csv('population_india_census2011.csv')


# In[89]:


df

