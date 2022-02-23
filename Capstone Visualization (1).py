#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# In[2]:


books=pd.read_csv('BOOKSCATALOGUE.CSV')
train=pd.read_csv('BOOKSMASTERTRAIN.CSV')
test=pd.read_csv('BOOKSMASTERTEST.CSV')
visit=pd.read_csv('BOOKSVISITHISTORY.CSV')
purchase=pd.read_csv('BOOKSPURCHHISTORY.CSV')
user=pd.read_csv('USERMASTER.CSV')


# In[3]:


train['USERRATINGS'].value_counts()


# In[4]:


# Visualize the count of ratings through histogram
train['USERRATINGS'] = train['USERRATINGS'].astype('int64')
sns.set_style('darkgrid')
fig, ax =plt.subplots()
fig.set_size_inches(9,6)
#a=np.arange(1925,2021,3)
#bins=np.arange(1925,2021,2),
sns.histplot(train['USERRATINGS'],color='y')
plt.ylabel('Count of each userrating')
plt.xlabel('Userrating')
plt.title('Visualizing the total count of each rating')
plt.show()


# ## Average rating distribution for top 10 books

# In[53]:


avg_total_rating=pd.DataFrame(train.groupby(['BOOKNAME','GENRE']).mean()['USERRATINGS'])
avg_total_rating.rename(columns={'USERRATINGS':'avgrating'},inplace=True)


# In[54]:


avg_total_rating


# In[55]:


sns.histplot(data=avg_total_rating, y="avgrating")


# In[56]:


sns.relplot(data=avg_total_rating, x="avgrating", y="GENRE") 


# In[57]:


#Visualize the distribution of ratings on basis of genre. Clearly Childrens-Picture Books is highest average rated genre
sns.jointplot(x="avgrating", y="GENRE", data=avg_total_rating, alpha=0.6,height=7,color='g')
plt.show()


# ## Top 10 highest rated books

# In[66]:


avg_total_rating['num_of_ratings']=train.groupby(['BOOKNAME','GENRE'])['USERRATINGS'].count()
avg_total_rating.sort_values(by=['num_of_ratings','avgrating'],ascending=False).head(10)


# In[64]:


sns.jointplot(x="num_of_ratings", y="GENRE", data=avg_total_rating, alpha=0.6,height=7,color='y')
plt.show()


# ## Relation between count of user ratings and average rating 

# In[61]:


sns.jointplot(x="avgrating", y="num_of_ratings", data=avg_total_rating, alpha=0.6,height=7,color='g')
plt.show()


# In[ ]:





# ### 10 most popular authors and there respective book

# In[69]:


#10 most popular author
popu_authors=pd.DataFrame(train.groupby(['AUTHOR','BOOKNAME']).count()['Popularity'])
popu_authors=popu_authors.sort_values(by='Popularity',ascending=False).head(10)


# In[76]:


popu_authors


# In[70]:


sns.relplot(data=popu_authors, x="Popularity", y="AUTHOR") 


# In[83]:


sns.lineplot(data=popu_authors,x='Popularity',y='AUTHOR')


# In[75]:


sns.jointplot(x="Popularity", y="BOOKNAME", data=popu_authors, alpha=0.6,height=7,color='g')
plt.show()


# ## 10 most popular books

# In[77]:


popu_books=pd.DataFrame(train.groupby(['BOOKNAME']).count()['Popularity'])
popu_books=popu_books.sort_values(by='Popularity',ascending=False).head(10)


# In[78]:


popu_books


# In[81]:


sns.lineplot(data=popu_books,x='Popularity',y='BOOKNAME')


# ## States and substates with most number of books 

# In[84]:


books.columns


# In[108]:


state_subs=books[['STATE','SUBSTATE']].value_counts()


# In[109]:


sns.stripplot(data=state_sub,x="STATE",y="SUBSTATE")


# ## Age group with most read books based on genre

# In[110]:


ages=user['AGEGROUP']
bins=[15,25,35,45,55,65,80]
labels=[1,2,3,4,5,6]
user['binned']=pd.cut(user['AGEGROUP'],bins,labels=labels)
user['binned'].value_counts()


# In[121]:


#How to get categories?
#user['binned'].categories----->giving error


# In[112]:


train_purch=pd.merge(train,purchase,on='BookID',how='inner')
train_user=pd.merge(train_purch,user,on='UserID',how='inner')


# In[119]:


booksbyage=pd.DataFrame(train_user.groupby(['GENRE','binned']).count()['Popularity'])
booksbyage.sort_values(by='Popularity',ascending=False)


# In[ ]:


#Fiction is most popular book for category 4 age group


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




