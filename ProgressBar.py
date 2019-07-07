#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Lib: https://pypi.org/project/progressbar2/
# pip install progressbar



import time
import progressbar

for i in progressbar.progressbar(range(100)):
    time.sleep(0.2)

    


# In[28]:


import time
import progressbar

for i in progressbar.progressbar(range(100), redirect_stdout=True):
    print('Some text', i)
    time.sleep(0.1)


# In[3]:


import time
import progressbar

bar = progressbar.ProgressBar(max_value=progressbar.UnknownLength)
for i in range(20):
    time.sleep(0.1)
    bar.update(i)


# In[30]:


import time
import progressbar

widgets=[
    ' [', progressbar.Timer(), '] ',
    progressbar.Bar(),
    ' (', progressbar.ETA(), ') ',
]
for i in progressbar.progressbar(range(20), widgets=widgets):
    time.sleep(0.1)

