#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install wordcloud')
get_ipython().system('pip install matplotlib')
get_ipython().system('pip install pillow')
get_ipython().system('pip install numpy')


# In[2]:


import numpy as np

import os
import re
from PIL import Image
from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import io


# In[3]:


mask = np.array(Image.open('C:/example/Color.png'))


# In[20]:


f = open('C:/example/kobartkkmamorph.txt','r',encoding = 'cp949')
txt = f.readlines()
f.close()


# In[21]:


new_txt=[]
for i in txt:
    new_txt.append(i.replace('\n',''))


# In[22]:


new_txt


# In[23]:


str_txt=''
for i in new_txt:
    str_txt = str_txt + i + ' '


# In[24]:


from collections import Counter
Counter(new_txt).most_common()


# In[29]:


stop = [',','을','의','.','이','적','','는','에','으로','들','를','과','위','가','있는','것','하는','이다','와','등','은','할','하고',
       '인','인가','에서는','따라서','무엇','로','해서는','그것','되고','즉','및','고도','대해','서는','다소','음로써','한다고',
       '다','예','로는','여서','이를','통해','에는','과의','에서','또한','그','된','하여','인지','하','ㄴ','고']
stopwords = set(stop)


# In[30]:


wc = WordCloud(font_path = 'C:/Windows/Fonts/이화체.ttf',max_words=1000, mask=mask, stopwords=stopwords, margin=10,
               random_state=1,contour_color='white').generate(str_txt)

wc.to_file("Kkma-morph.png")
plt.axis("off")
plt.figure(figsize=(10,10))
plt.title("Default colors")
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()


# In[ ]:




