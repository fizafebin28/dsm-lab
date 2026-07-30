#!/usr/bin/env python
# coding: utf-8

# In[21]:


import numpy as np
a=np.array([[1,2],[3,4]])
b=np.array([[2,4],[6,8]])

print("Addition: \n",a+b)
print("\nSubtraction: \n",a-b)
print("\nNormal Multi: \n",a*b)
print("\nDivision: \n",a/b)
print("\nMultiplication: \n",np.dot(a,b))#a@b also can use
print("\nTranspose of a: \n",np.transpose(a))
print("\nTranspose of b: \n",np.transpose(b))


# In[23]:


import numpy as np
X=np.array([[1,2],[3,4]])

U,S,VT=np.linalg.svd(X)

n_components=2

X_reconstructed=np.dot(U[:,:n_components],np.dot(np.diag(S[:n_components]),VT[:n_components,:]))
print("Original matrix: ")
print(X)
print("\nReconstructed Matrix(with reduced dimensions): ")
print(X_reconstructed)


# In[40]:


import matplotlib.pyplot as plt
x=[3,5,6]
y=[1,4,7]
plt.plot(x,y,)
plt.title("PLOT")
plt.xlabel("size")
plt.ylabel("time")


# In[43]:


import matplotlib.pyplot as plt
subjects=["English","Maths","Computer"]
marks=[89,87,95]
plt.bar(subjects,marks)
plt.title("BAR")
plt.xlabel("subject")
plt.ylabel("mark")


# In[42]:


import matplotlib.pyplot as plt
subjects=["English","Maths","Computer"]
marks=[89,87,95]
plt.scatter(subjects,marks)
plt.title("SCATTER")
plt.xlabel("subject")
plt.ylabel("mark")


# In[41]:


import matplotlib.pyplot as plt
subjects=["English","Maths","Computer"]
marks=[10,20,20,20,30,30,30,30,40,50]
plt.hist(marks)
plt.title("HISTOGRAM")
plt.xlabel("subject")
plt.ylabel("mark")
plt.legend("profit")


# In[50]:


import matplotlib.pyplot as plt
marks=[30,40,50]
subjects=["English","Maths","Computer"]
plt.pie(marks,labels=subjects)
plt.title("PIE CHART")


# In[56]:


import matplotlib.pyplot as plt
x=[1,2,6,18]
y=[3,10,12,20]
plt.plot(x,y,'r:o')
plt.title("LINE PLOT")
#plt.xlabel("size")
#plt.ylabel("time")


# In[72]:


import matplotlib.pyplot as plt
plt.suptitle("MULTIPLE PLOT")
plt.subplot(1,2,1)
plt.plot((1,2,3),(2,4,6))

plt.subplot(1,2,2)
plt.plot((1,2,3),(1,3,5))



# In[ ]:




