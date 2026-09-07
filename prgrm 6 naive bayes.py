#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np 
from sklearn import datasets,metrics
from sklearn.model_selection import train_test_split  
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score 

iris=datasets.load_iris()
X=iris.data
y=iris.target
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42) 
nb_classifier=GaussianNB()
nb_classifier.fit(X_train,y_train)
y_pred=nb_classifier.predict(X_test)
accuracy = accuracy_score(y_test,y_pred) 
print(accuracy)
print(f"Accuracy:{accuracy*100:.2f}%")


# In[4]:


import pandas as pd
from sklearn.model_selection import train_test_split  
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score 

data={'Sweetness':[10,1,10,7,3,1,2,3,8,3,1,3,7,10,2],
      'Crunchiness':[9,4,1,10,10,1,8,1,5,7,3,6,3,7,3],
      'FoodType':['fruit','protein','fruit','vegetable','vegetable','protein','vegetable','protein','fruit','vegetable','vegetable','protein','fruit','fruit','protein']}
df=pd.DataFrame(data)

X=df[['Sweetness','Crunchiness']]
y=df['FoodType']

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
model=GaussianNB()
model.fit(X_train,y_train)

y_pred=model.predict(X_test)

accuracy=accuracy_score(y_test,y_pred)

print("Predicted:",y_pred)
print("Accuracy:",accuracy*100,"%")


# In[13]:


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split  
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder 

data = pd.read_csv('food.csv') 
X = data.iloc[:, :3] 
print(X) 
y= data.iloc[:, 3]

le = LabelEncoder() 
categorical_columns = ['Ingredient']   
for col in categorical_columns: 
    X[col] = le.fit_transform(X[col]) 
y = le.fit_transform(y) 

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42) 
k=3 
nb = GaussianNB() 
nb.fit(X_train,y_train) 
y_pred = nb.predict(X_test)

sample=[[1,10,9]] 
k=nb.predict(sample) 
print(k) 
accuracy = accuracy_score(y_test,y_pred) 
print("Accuracy:",accuracy)


# In[12]:


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

data=pd.read_csv('cricket.csv')
X=data.iloc[:,:5]
print(X)
y=data.iloc[:,4]
print(y)

le=LabelEncoder()
categorical_columns=['Outlook','Temp','Humidity','Windy','Play Cricket']
for col in categorical_columns:
    X[col]=le.fit_transform(X[col])
y=le.fit_transform(y)
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42) 
k=3 
nb = GaussianNB() 
nb.fit(X_train,y_train) 
y_pred = nb.predict(X_test)

sample=[[1,10,9,11,4]] 
k=nb.predict(sample) 
print(k) 
accuracy = accuracy_score(y_test,y_pred) 
print("Accuracy:",accuracy)


# In[14]:


import numpy as np  
import pandas as pd 
from sklearn.model_selection import train_test_split  
from sklearn.naive_bayes import GaussianNB 
from sklearn.metrics import accuracy_score 

data = pd.read_csv('insurance.csv') 
X = data.iloc[:, :6] 
print(X) 
y= data.iloc[:, 1] 
le = LabelEncoder() 
categorical_columns = ['sex', 'smoker', 'region']   
for col in categorical_columns: 
 X[col] = le.fit_transform(X[col]) 
y = le.fit_transform(y) 

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42) 
k=3 
nb = GaussianNB() 
nb.fit(X_train,y_train) 
y_pred = nb.predict(X_test) 
sample=[[1,10,9,11,4,2]] 
k=nb.predict(sample) 
print(k) 
accuracy = accuracy_score(y_test,y_pred) 
print("Accuracy:",accuracy)


# In[ ]:




