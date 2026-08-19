#!/usr/bin/env python
# coding: utf-8

# In[36]:


from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
iris=load_iris()
X=iris.data
y=iris.target
print("Features= ",iris.feature_names)
print("Target= ",iris.target_names)
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
knn=KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train,y_train)
y_predict=knn.predict(X_test)
accuracy=accuracy_score(y_test,y_predict)
print(f'Accuracy= {accuracy:.2f}')
print("Prediction=",y_predict[0])
new=[[1.1,2.2,3.3,4.4]]
new_predict=knn.predict(new)
print("Target name= ",iris.target_names[new_predict])


# In[42]:


from sklearn.datasets import load_breast_cancer
cancer=load_breast_cancer()
X=cancer.data
y=cancer.target
print("Features= ",cancer.feature_names)
print("Target= ",cancer.target_names)
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
knn=KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train,y_train)
y_predict=knn.predict(X_test)
accuracy=accuracy_score(y_test,y_predict)
print(f'Accuracy= {accuracy:.2f}')
print("Prediction=",y_predict[0])
new=[[18.50, 22.50, 123.00, 1050.00, 0.105, 0.180, 0.220, 0.120, 0.210, 0.065, 0.600, 1.200, 4.000, 70.000, 0.008, 0.035, 0.050, 0.020, 0.030, 0.006, 23.00, 30.00, 155.00, 1600.00, 0.145, 0.400, 0.500, 0.220, 0.300, 0.090]]
new_predict=knn.predict(new)
print("Target name= ",cancer.target_names[new_predict])


# In[ ]:




