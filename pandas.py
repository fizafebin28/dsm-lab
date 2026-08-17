#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
dict={'rollno':[1,2,3,4],'name':['one','two','three','four']}
#print(dict)
b=pd.DataFrame(dict)
print(b)


# In[6]:


a=[1,2,3,4]
b=pd.Series(a)
print(b)


# In[8]:


a=[1,2,3,4]
b=pd.Series(a,index=['a','b','c','d'])
print(b)


# In[12]:


import pandas as pd
dict={'rollno':[1,2,3,4],'name':['one','two','three','four']}
b=pd.DataFrame(dict)
print(b.loc[0])


# In[ ]:


import pandas as pd
dict={'rollno':[1,2,3,4],'name':['one','two','three','four']}
b=pd.DataFrame(dict)
print(b.loc[0,])


# In[2]:


import pandas as pd
a=pd.read_csv('fruit.csv')
print(a)


# In[9]:


import pandas as pd
a=pd.read_csv('fruit.csv')
print("Tail(2):\n",a.tail(2),"\n")
print("Head(2):\n",a.head(2))


# In[30]:


import pandas as pd
a=pd.read_csv('fruit.csv')
b=a.dropna()
print(b)


# In[18]:


import pandas as pd
lst=[10,20,30,40,50]
a=pd.Series(lst)
print(a)


# In[19]:


import pandas as pd
a=pd.date_range(start='20-11-2024',end='24-11-2024')
print(a)


# In[20]:


import pandas as pd
a=[[1,'Anu',20],[2,'Ammu',21],[3,'Riya',22]]
df=pd.DataFrame(a)
print(df)


# In[21]:


import pandas as pd
a={'Name':['Anu','Ammu','Riya'],'Age':[20,21,22]}
df=pd.DataFrame(a)
print(df)


# In[22]:


import pandas as pd
a={'Name':['Anu','Ammu','Riya','John','Arun','Sara'],'Age':[20,21,22,23,24,25]}
df=pd.DataFrame(a)

print("Head:\n",df.head(),"\n")
print("Tail:\n",df.tail())


# In[27]:


import pandas as pd
a={'Name':['Anu','Ammu','Riya','John','Arun','Sara'],'Age':[20,21,22,23,24,25]}
df=pd.DataFrame(a)
print(df.loc[[0,1]])


# In[28]:


import pandas as pd
import numpy as np
a={'Name':['Anu','Ammu','Riya','John'],'Age':[20,np.nan,22,23]}
df=pd.DataFrame(a)
print("Before:\n",df)
df=df.fillna(0)
print("After:\n",df)

