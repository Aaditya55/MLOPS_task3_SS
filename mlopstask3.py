#!/usr/bin/env python
# coding: utf-8



from parameters import *
import pandas as pd


# In[2]:


dataset = pd.read_csv('Churn_Modelling.csv')


# In[3]:


dataset.columns


# In[4]:


y = dataset['Exited']


# In[ ]:





# In[5]:


X = dataset[['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard',
       'IsActiveMember', 'EstimatedSalary']]


# In[6]:


geo = dataset['Geography']


# In[7]:


geo = pd.get_dummies(geo, drop_first=True )


# In[8]:


gender = dataset['Gender']


# In[9]:


gender = pd.get_dummies(gender, drop_first=True )


# In[10]:


X = pd.concat([X,gender,geo], axis=1)


# In[11]:


X.info()


# In[12]:


from keras.optimizers import Adam


# In[13]:


from keras import metrics


# In[14]:


from sklearn.model_selection import train_test_split


# In[15]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)


# In[16]:


from keras.models import Sequential


# In[17]:




# In[18]:


from keras.layers import Dense

import tensorflow as tf
tf.get_logger().setLevel('ERROR')


# In[19]:
model =Sequential()

model.add(Dense(units=6, input_dim=11, activation='relu' ))


# In[20]:


model.add(Dense(units=3, activation='relu'))


# In[21]:


#model.add(Dense(units=2, activation='relu'))


# In[22]:


#model.add(Dense(units=2,  activation='relu' ))


# In[23]:


model.add(Dense(units=1,  activation='relu' ))


# In[24]:




# In[25]:


model.compile(optimizer=Adam(learning_rate=var_lr),loss='binary_crossentropy',metrics=['accuracy'])


# In[26]:


#model.summary()


# In[34]:


history=model.fit(X_train,y_train , epochs=10 , verbose=0) #aresok


# In[38]:


print(history.history['accuracy'][9])


# In[28]:


