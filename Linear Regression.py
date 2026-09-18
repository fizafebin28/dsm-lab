#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split    
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.linear_model import LinearRegression

data=load_iris()
X=data.data[:, 2].reshape(-1,1)
y=data.target

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

lr_model=LinearRegression()
lr_model.fit(X_train,y_train)

lr_predict=lr_model.predict(X_test)
lr_mse=mean_squared_error(y_test,lr_predict)
print(f'Linear Regression MSE: {lr_mse}')
r2_score=r2_score(y_test,lr_predict)
print('R2 Score: ',r2_score)

new_predict=[[5.1]]
prediction=lr_model.predict(new_predict)

predicted_class=round(prediction[0])
print(f"Predicted: ",data.target_names[predicted_class])


# In[4]:


# import numpy as np
# import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split     
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.linear_model import LinearRegression

data=load_iris()
X=data.data
y=data.target

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

model=LinearRegression()
model.fit(X_train,y_train)

y_predict=model.predict(X_test)

mse=mean_squared_error(y_test,y_predict)
print(f'Linear Regression MSE: {mse}')

r2=r2_score(y_test,y_predict)
print('R2 Score: ',r2)

new_predict=[[5.1,3.5,1.4,0.2]]
prediction=model.predict(new_predict)

predicted_class=round(prediction[0])
print(f"Predicted: ",data.target_names[predicted_class])


# In[ ]:




