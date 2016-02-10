
# coding: utf-8

# In[1]:

import pandas as pd
from pandas import Series,DataFrame
import numpy as np

# For Visualization
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
get_ipython().magic('matplotlib inline')

# For reading stock data from yahoo
from pandas.io.data import DataReader

# For time stamps
from datetime import datetime

# For division
from __future__ import division


# In[2]:

# The tech stocks we'll use for this analysis
tech_list = ['AAPL','GOOG','MSFT','AMZN','LNKD']

# Set up End and Start times for data grab
end = datetime.now()
start = datetime(end.year - 1,end.month,end.day)


#For loop for grabing yahoo finance data and setting as a dataframe

for stock in tech_list:   
    # Set DataFrame as the Stock Ticker
    globals()[stock] = DataReader(stock,'yahoo',start,end)


# In[3]:

LNKD.describe()


# In[4]:

LNKD.info()


# In[5]:

# Let's see a historical view of the closing price
LNKD['Adj Close'].plot(legend=True,figsize=(10,4))


# In[6]:

# Now let's plot the total volume of stock being traded each day over the past 5 years
LNKD['Volume'].plot(legend=True,figsize=(10,4))


# In[7]:



#  plot out several moving averages
ma_day = [10,20,50]

for ma in ma_day:
    column_name = "MA for %s days" %(str(ma))
    LNKD[column_name]=pd.rolling_mean(AAPL['Adj Close'],ma)


# In[8]:

LNKD[['Adj Close','MA for 10 days','MA for 20 days','MA for 50 days']].plot(subplots=False,figsize=(10,4))


# In[9]:

# 
LNKD['Daily Return'] = LNKD['Adj Close'].pct_change()
# plot the daily return percentage
LNKD['Daily Return'].plot(figsize=(12,4),legend=True,linestyle='--',marker='o')


# In[10]:


sns.distplot(LNKD['Daily Return'].dropna(),bins=100,color='purple')

# Could have also done:
#AAPL['Daily Return'].hist()


# In[11]:

# Could have also done:
LNKD['Daily Return'].hist()


# In[12]:

# Grab all the closing prices for the tech stock list into one DataFrame
closing_df = DataReader(['AAPL','GOOG','MSFT','AMZN','LNKD'],'yahoo',start,end)['Adj Close']


# In[13]:

# Make a new tech returns DataFrame
tech_rets = closing_df.pct_change()


# In[14]:

sns.jointplot('GOOG','MSFT',tech_rets,kind='scatter')


# In[15]:

from IPython.display import SVG
SVG(url='http://upload.wikimedia.org/wikipedia/commons/d/d4/Correlation_examples2.svg')


# In[16]:

sns.pairplot(tech_rets.dropna())


# In[17]:


returns_fig = sns.PairGrid(closing_df)


returns_fig.map_upper(plt.scatter,color='purple')

#  the lower triangle in the figure, inclufing the plot type (kde) or the color map (BluePurple)
returns_fig.map_lower(sns.kdeplot,cmap='cool_d')

#  a series of histogram plots of the closing price
returns_fig.map_diag(plt.hist,bins=30)


# In[18]:

sns.corrplot(tech_rets.dropna(),annot=True)


# In[ ]:



