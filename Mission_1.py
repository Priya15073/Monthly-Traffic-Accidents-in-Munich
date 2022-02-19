#!/usr/bin/env python
# coding: utf-8

# # Installing Libraries

# In[1]:


get_ipython().system('pip3 install numpy pandas matplotlib')


# In[2]:


get_ipython().system('pip3 install sklearn')


# In[3]:


get_ipython().system('pip3 install statsmodels')


# # Data Preparation

# In[4]:


#Loading data
import pandas as pd
traffic_accidents=pd.read_csv("210619monatszahlenjuni2021monatszahlen2106verkehrsunfaelle.csv")
print(traffic_accidents.head(5))


# In[5]:


df=traffic_accidents[['MONATSZAHL','AUSPRAEGUNG','JAHR','MONAT','WERT']]
print(df.head(10))


# In[6]:


# Removing Empty Cells
df=df.dropna()

df1=df[df['MONAT']=='Summe']

df1.head(10)


# In[7]:


df=df[df['MONAT']!='Summe']
df['MONAT']=df['MONAT'].str[4:]

df.head(10)


# # Data Visualization

# In[8]:


#Visualizing number of accidents by category
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(20,10))
# use unstack()
df1.groupby(['JAHR','MONATSZAHL']).mean()['WERT'].unstack().plot(ax=ax)
ax.set_xlabel('Year')
ax.set_ylabel('Number of accidents')
fig.suptitle('Number of accidents per year category wise', fontsize=20)
fig.savefig('by_year.jpg')
plt.show()


# In[9]:


df1.groupby(['JAHR','MONATSZAHL']).mean()['WERT'].unstack()
print(df1)


# In[10]:


df.info()


# In[11]:


fig1, ax = plt.subplots(figsize=(20,10))
# use unstack()
df.groupby(['JAHR','MONAT','MONATSZAHL']).mean()['WERT'].unstack().plot(ax=ax)
ax.set_xlabel('Year+Month')
ax.set_ylabel('Number of accidents')
fig.suptitle('Number of accidents per month category wise', fontsize=20)
fig.savefig('by_month.jpg')
plt.show()


# # Data Processing and Models

# In[12]:


#encoding string data
from sklearn import preprocessing
label_encoder = preprocessing.LabelEncoder()
df['MONATSZAHL']= label_encoder.fit_transform(df['MONATSZAHL'])
df['AUSPRAEGUNG']= label_encoder.fit_transform(df['AUSPRAEGUNG'])
df['MONATSZAHL'].unique()
df['AUSPRAEGUNG'].unique()
print(df)


# In[13]:


#Assigning X and Y
print(df.shape)
X= df.drop(['WERT'],axis=1)
Y= df['WERT']
print(X.shape,Y.shape)


# In[14]:


#Linear Regression
from sklearn.linear_model import LinearRegression
model_lr= LinearRegression()
model_lr.fit(X,Y)
pred_lr=model_lr.predict(X)
plt.plot(df.index,Y)
plt.plot(df.index,pred_lr)
plt.show()


# In[15]:


#Random Forest
from sklearn.ensemble import RandomForestRegressor
model_rf=RandomForestRegressor()
model_rf.fit(X,Y)
pred_rf=model_rf.predict(X)
plt.plot(df.index,Y)
plt.plot(df.index,pred_rf)
plt.show()


# In[16]:


import pickle
#Saving the model
print("Saving the model...")
with open("Model_RF.pkl","wb") as f:
    pickle.dump(model_rf,f)
print("Model saved!")


# In[17]:


from joblib import dump, load
dump(model_rf , 'model_rf.joblib')


# In[21]:


# Prediction for Category: 'Alkoholunfälle'
# Type: 'insgesamt
# Year: '2021'
# Month: '01'
print("Prediction for Alkoholunfalle,insgesamt,2021,01"+str(model_rf.predict([[0,1,'2021','01']])))


# In[ ]:




