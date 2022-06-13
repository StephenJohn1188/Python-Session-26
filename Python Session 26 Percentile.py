#!/usr/bin/env python
# coding: utf-8

# import numpy as np

# In[2]:


import numpy as np


# In[3]:


a=np.array([1,2,3,4,5,6,6,7,8,8])
np.percentile(a,50)


# In[4]:


np.percentile(a,25)


# In[8]:


import pandas as pd
data=pd.read_csv('president_heights.csv')


# In[9]:


data


# In[10]:


heights=data['height']


# In[11]:


print('Mean Height:',heights.mean())
print('Standard Deviation:',heights.std())
print('Minimum Height:',heights.min())
print('Maximum Height:',heights.max())


# In[13]:


print('25th Percentile:',np.percentile(heights, 25))


# In[15]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[17]:


plt.hist(heights)
plt.title('Height distribution of US presidents')
plt.xlabel('Height(cm)')
plt.ylabel('number')


# # Scipy gives all statistical functions

# In[20]:


import scipy
import numpy as np
import warnings
warnings.filterwarnings('ignore')


# In[21]:


j=np.array([[12,45,48],[89,56,23],[75,53,15]])
j


# In[25]:


round(scipy.mean(j))


# In[24]:


scipy.var(a)


# In[29]:


import scipy.stats as st
j=np.array([12,45,48,89,56,23, 75,53,15])
st.mode(j)


# In[30]:


from scipy.stats import zscore


# In[31]:


zscore([23,34,45,56,67,78])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




