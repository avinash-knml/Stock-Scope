#!/usr/bin/env python
# In[1]:

import streamlit as st 
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')


# In[2]:

st.set_page_config(
    page_title="Stock Scope",
    page_icon="📈",
    layout="wide")

st.title('Stock Scope')

data=pd.read_csv(r'data\nifty.csv')


# In[3]:


data.columns=data.columns.str.lower()
data.columns=data.columns.str.replace('\n','')
data.columns=data.columns.str.replace(' ','')


# In[4]:


data=data[['symbol', 'ltp', 'volume(shares)', 'value(₹crores)','52wh']]
data=data.rename(columns={'volume(shares)':'volume',
                          'value(₹crores)':'value'})


# In[5]:


cols=['ltp', 'volume', 'value', '52wh']
for i in cols:
    data[i]=data[i].str.replace(',','', regex=True)
    data[i]=pd.to_numeric(data[i])


# In[10]:

percentage=st.slider('Enter your prefered percentage: ', 0, 10,1)
st.write('Prefered Percentage: ',percentage)
x=data['ltp']*(percentage/100)
data['52wh-x']=data['52wh']-x


# In[11]:


final=data[data['ltp']>=data['52wh-x']].reset_index(drop=True)
final=final[['symbol', 'ltp', 'volume', 'value']]
#st.table(final)

# In[12]

symbols = final['symbol'].tolist()
ltp=final['ltp'].tolist()

cols_per_row = 4

for i in range(0, len(symbols), cols_per_row):
    cols = st.columns(cols_per_row)

    for j, symbol in enumerate(symbols[i:i + cols_per_row]):
        with cols[j]:
            with st.container(border=True):
                st.markdown(f"### {symbol}")
                