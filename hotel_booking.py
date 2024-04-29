#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
import os


# In[2]:


os.getcwd()


# In[3]:


os.chdir('C:\\Users\\Abhi\\documents\\readings')


# In[4]:


df=pd.read_csv('hotel_booking.csv')


# In[5]:


df.head()


# In[8]:


df.drop(['name','email','phone-number','credit_card'],axis=1,inplace=True)


# In[9]:


df.shape


# In[10]:


df.dtypes


# In[5]:


df['reservation_status_date'] =pd.to_datetime(df['reservation_status_date'])


# In[6]:


df.describe(include='object')


# In[7]:


for col in df.describe(include='object').columns:
    print(col)
    print(df[col].unique())
    print('-'*50)


# In[8]:


df.isnull().sum()


# In[9]:


df.drop(['agent','company'],axis=1,inplace=True)
df.dropna(inplace=True)
df.isnull().sum()


# In[10]:


df.describe()


# In[11]:


df['adr'].plot(kind='box')


# In[12]:


df=df[df['adr']<5000]


# # Data Analysis

# In[13]:


canceled_perc=df['is_canceled'].value_counts(normalize =True)
canceled_perc


# In[14]:


canceled_perc
print(canceled_perc)
plt.figure(figsize=(6,5))
plt.title('Reservation status count')
plt.bar(['Not_canceled','is_canceled'],df['is_canceled'].value_counts(),edgecolor='k',width=0.7)
plt.show()


# In[15]:


plt.figure(figsize=(8,4))
axl=sns.countplot(x='hotel',hue='is_canceled',data=df,palette='Blues')
legend_labels,_=axl.get_legend_handles_labels()
plt.title('Reservation status in different hotels',size=20)
plt.xlabel(['hotel'])
plt.legend(['not_canceled','canceled'])
plt.show()


# In[12]:


resort_hotel=df[df['hotel'] =='Resort Hotel']
resort_hotel['is_canceled'].value_counts(normalize=True)


# In[35]:


import warnings
warnings.filterwarnings("ignore")


# In[13]:


city_hotel=df[df['hotel'] =='City Hotel']
city_hotel['is_canceled'].value_counts(normalize=True)


# In[6]:


pd.set_option("display.max.rows",None)
pd.set_option("display.max.columns",None)


# In[32]:


df['reservation_status_date'] = pd.to_datetime(df['reservation_status_date'])


# In[33]:


df["reservation_status_date"].dtype


# In[8]:


df["adr"].describe().to_frame().T


# In[14]:


resort_hotel["adr"].describe().to_frame().T


# In[15]:


city_hotel["adr"].describe().to_frame().T


# In[29]:


resort_hotel = df[df["hotel"]=="Resort Hotel"]
city_hotel = df[df["hotel"]=="City Hotel"]
print(resort_hotel.shape,city_hotel.shape)


# In[20]:


resort_hotel_final =resort_hotel.groupby('reservation_status_date')[['adr']].mean()
city_hotel_final =resort_hotel.groupby('reservation_status_date')[['adr']].mean()


# In[38]:


plt.figure(figsize=(15,6))
plt.plot(resort_hotel_final.index,resort_hotel_final.values,label="Resort_Hotel",color="orange")
plt.xticks(ticks=None)
plt.legend()
plt.show()


# In[41]:


plt.figure(figsize=(15,6))
plt.plot(city_hotel_final.index,city_hotel_final.values,label="City Hotel",color="royalblue")
plt.xticks(ticks=None)
plt.legend()
plt.show()


# In[ ]:


plt.figure(figsize=(15,6))
plt.plot(resort_hotel_final.index,resort_hotel_final.values,label="Resort_Hotel",color="red")
plt.plot(city_hotel_final.index,city_hotel_final.values,label="City Hotel",color="blue")
plt.xticks(ticks=None)
plt.legend()
plt.show()


# In[31]:


plt.figure(figsize=(15,7))
plt.title('Average daily in city and resort hotel',fontsize=30)
plt.plot(resort_hotel_final.index,resort_hotel_final['adr'],label='Resort Hotel')
plt.plot(city_hotel_final.index,city_hotel_final['adr'],label='City Hotel')
plt.legend(fontsize=20)
plt.show()


# In[20]:


df['month']=df['reservation_status_date'].dt.month
plt.figure(figsize=(12,6))
axl=sns.countplot(x='month',hue='is_canceled',data=df)
plt.title('Reservation status per month',size=20)
plt.xlabel('month')
plt.ylabel('number of reservations')
plt.legend(['not canceled','canceled'])
plt.show()


# In[51]:


plt.figure(figsize=(10,6))
plt.title('ADR per month',fontsize=30)
sns.barplot(x='month',y='adr',color='blue',data = df[df['is_canceled']==1].groupby('month')[['adr']].sum().reset_index())
plt.legend(fontsize=15)
plt.show()


# In[41]:


canceled_df=df[df['is_canceled']==1]
top_10_country=canceled_df['country'].value_counts()[:10]
plt.figure(figsize=(6,5))  
plt.title('Top 10 countries with reservative canceled')
plt.pie(top_10_country,autopct='%.2f',labels=top_10_country.index)
plt.show()


# In[22]:


df['market_segment'].value_counts()


# In[23]:


df['market_segment'].value_counts(normalize=True)


# In[27]:


canceled_df=df['market_segment'].value_counts(normalize=True)
canceled_df


# In[31]:


canceled_df=df[df['is_canceled']==1]


# In[32]:


canceled_df_adr = canceled_df.groupby('is_canceled')[['adr']].mean()
canceled_df_adr


# In[33]:


canceled_df_adr=canceled_df.groupby('reservation_status_date')[['adr']].mean()
canceled_df_adr.reset_index(inplace=True)
canceled_df_adr.sort_values('reservation_status_date',inplace=True)

not_canceled_df=df[df['is_canceled']==0]
not_canceled_df_adr=not_canceled_df.groupby('reservation_status_date')[['adr']].mean()
not_canceled_df_adr.reset_index(inplace=True)
not_canceled_df_adr.sort_values('reservation_status_date',inplace=True)

plt.figure(figsize=(20,6))
plt.title('Average Daily Rate')
plt.plot(not_canceled_df_adr['reservation_status_date'],not_canceled_df_adr['adr'],label='not_canceled')
plt.plot(canceled_df_adr['reservation_status_date'],canceled_df_adr['adr'],label='canceled')
plt.legend()


# In[37]:


canceled_df_adr=canceled_df_adr[(canceled_df_adr['reservation_status_date']>'2016') & (canceled_df_adr['reservation_status_date']<'2017-09')]
not_canceled_df_adr=not_canceled_df_adr[(not_canceled_df_adr['reservation_status_date']>'2016') & (not_canceled_df_adr['reservation_status_date']<'2017-09')]


# In[50]:


plt.figure(figsize=(15,5))
plt.title('Average Daily Rate')
plt.plot(not_canceled_df_adr['reservation_status_date'],not_canceled_df_adr['adr'],label='not_canceled')
plt.plot(canceled_df_adr['reservation_status_date'],canceled_df_adr['adr'],label='canceled')
plt.legend(fontsize=20)


# In[ ]:





# In[ ]:





# In[ ]:




