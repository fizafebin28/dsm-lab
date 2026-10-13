#!/usr/bin/env python
# coding: utf-8

# In[12]:


import numpy as np
import matplotlib.pyplot  as plt
from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

data = load_iris()
X= data.data
y= data.target
X_train,X_test,y_train,y_test= train_test_split(X,y,test_size=0.2,random_state=42)
dt_model = DecisionTreeClassifier()
dt_model.fit(X_train,y_train) 
plt.figure(figsize=(12,8))
tree.plot_tree(dt_model,fontsize=10)
y_pred = dt_model.predict(X_test)
accuracy = accuracy_score(y_test,y_pred)
print(f'Accuracy of Decision Tree Model: {accuracy:2f}')


# In[13]:


import numpy as np
import matplotlib.pyplot  as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.metrics import accuracy_score

data = load_iris()
X= data.data
y= data.target
X_train,X_test,y_train,y_test= train_test_split(X,y,test_size=0.2,random_state=42)
dt_model = DecisionTreeClassifier()
dt_model.fit(X_train,y_train) 
plt.figure(figsize=(18,13))
plot_tree(dt_model,feature_names=data.feature_names,class_names=data.target_names,filled=True,fontsize=12)
y_pred = dt_model.predict(X_test)
accuracy = accuracy_score(y_test,y_pred)
print(f'Accuracy of Decision Tree Model: {accuracy:2f}')


# In[ ]:




