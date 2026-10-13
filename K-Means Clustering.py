#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import matplotlib.pyplot  as plt
from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score

data = load_iris()
X= data.data
y= data.target
X_train,X_test,y_train,y_test= train_test_split(X,y,test_size=0.2,random_state=42)
model = KMeans(n_clusters=3,random_state=42)
model.fit(X_train)
y_pred=model.predict(X_test)

plt.scatter(X_train[:,0],X_train[:,1],c=model.labels_)
plt.scatter(model.cluster_centers_[:,0],model.cluster_centers_[:,1],marker='X',s=200)
plt.xlabel(data.feature_names[0])
plt.ylabel(data.feature_names[1])
plt.title("K-Means Clustering",c='black',fontsize=20,fontweight='bold')
plt.show()


# In[ ]:




