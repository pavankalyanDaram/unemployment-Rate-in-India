#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

data = pd.read_csv("unemployment.csv")
print(data.head())


# In[2]:


print(data.isnull().sum())


# In[3]:


data.columns= ["States","Date","Frequency",
               "Estimated Unemployment Rate",
               "Estimated Employed",
               "Estimated Labour Participation Rate",
               "Region","longitude","latitude"]


# In[4]:


plt.figure(figsize=(12,10))
plt.title("Indian Unemployment")
sns.histplot(x="Estimated Employed", hue="Region", data=data)
plt.show()


# In[5]:


plt.figure(figsize=(12, 10))
plt.title("Indian Unemployment")
sns.histplot(x="Estimated Unemployment Rate", hue="Region", data=data)
plt.show()


# In[6]:


plt.style.use('seaborn-whitegrid')
plt.figure(figsize=(12, 10))
sns.heatmap(data.corr())
plt.show()


# In[7]:


plt.figure(figsize=(12, 10))
plt.title("Indian Unemployment Rate In Each Date")
plt.xlabel("Estimated Unemployment Rate")
plt.ylabel("Date")
sns.histplot(x="Estimated Unemployment Rate", y="Date", data=data)
plt.show()


# In[8]:


unemploment = data[["States", "Region", "Estimated Unemployment Rate"]]
figure = px.sunburst(unemploment, path=["Region", "States"], 
                     values="Estimated Unemployment Rate", 
                     width=700, height=700, color_continuous_scale="hsv", 
                     title="Unemployment Rate in India")
figure.show()


# In[ ]:




