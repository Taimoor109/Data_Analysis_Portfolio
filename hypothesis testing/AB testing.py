#!/usr/bin/env python
# coding: utf-8

# # ** A/B test**

# In[1]:


import pandas as pd
from scipy import stats


# In[2]:


taxi_data = pd.read_csv("2017_Yellow_Taxi_Trip_Data.csv", index_col = 0)


# In[3]:


# descriptive stats code for EDA
taxi_data.describe(include='all')


# In[4]:


taxi_data.groupby('payment_type')['total_amount'].mean()


# In[5]:


#hypothesis test, A/B test
#significance level

credit_card = taxi_data[taxi_data['payment_type'] == 1]['total_amount']
cash = taxi_data[taxi_data['payment_type'] == 2]['total_amount']
stats.ttest_ind(a=credit_card, b=cash, equal_var=False)

