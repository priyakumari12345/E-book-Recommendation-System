#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
path1=r"C:\Users\priyakumari56\Documents\capstone project\Capstone6_Book Recommendation\bookscatalogue.csv"
path5=r"C:\Users\priyakumari56\Documents\capstone project\Capstone6_Book Recommendation\purchasehistory.csv"
path6=r"C:\Users\priyakumari56\Documents\capstone project\Capstone6_Book Recommendation\USERMASTER.csv"
path2=r"C:\Users\priyakumari56\Documents\capstone project\Capstone6_Book Recommendation\books_master_test.csv"
path3=r"C:\Users\priyakumari56\Documents\capstone project\Capstone6_Book Recommendation\books_master_train.csv"
path4=r"C:\Users\priyakumari56\Documents\capstone project\Capstone6_Book Recommendation\books_visit_history.csv"


# In[2]:


df1=pd.read_csv(path1)
df2=pd.read_csv(path2)
df3=pd.read_csv(path3)
df4=pd.read_csv(path4)
df5=pd.read_csv(path5)
df6=pd.read_csv(path6)


# # books catalogue

# In[3]:


df1.columns


# In[4]:


df1.count()


# In[5]:


#unique books----->4966
df1.nunique()


# In[6]:


df1.isna().sum()


# # booksmastertest+train

# In[7]:


#mastertest
df2.columns


# In[8]:


df2.count()


# In[9]:


df2.nunique()


# In[10]:


#booksmastertrain
df3.count()


# In[11]:


df3.nunique()


# In[12]:


#totalbooksmaster---->df4
dfcon=pd.concat([df2,df3],axis=0)


# In[13]:


dfcon.count()


# In[71]:


dfcon.describe()


# # max rating is given to which book

# In[74]:


max_rating=dfcon['USERRATINGS'].max()
dfcon['GENRE'][dfcon['USERRATINGS']==max_rating]


# In[14]:


#bookname and authordesc whose user ratings range between 3.5 to 4.5
dfcon[['BOOKNAME','AUTHORDESC','USERRATINGS']][(dfcon['USERRATINGS']<4.5) & (dfcon['USERRATINGS']>3.5)]


# In[15]:


dfcon.nunique()


# In[16]:


#extract books that have received ratings more than 3.5 
dfcon[['BookID','USERRATINGS']][dfcon['USERRATINGS']>3.5].sort_values('USERRATINGS',ascending=False).head(20)


# In[17]:


dfcon[['BOOKTITLE','AUTHORDESC','SUMMARY']].head(1)


# In[18]:


#author description for any 1 book with user ratings more than 4.5
dfcon[['BookID','AUTHORDESC','USERRATINGS']][dfcon['USERRATINGS']>4.5].head(1)


# ### Top 5 highest rated books, there genre and author

# In[75]:


dfcon[['BOOKNAME','GENRE','AUTHOR','USERRATINGS']].sort_values('USERRATINGS',ascending=False).head(5)


# ### Top 5 books based on popularity

# In[76]:


dfcon[['BookID','USERRATINGS','Popularity','AUTHOR','GENRE']].sort_values('Popularity',ascending=False).head(5)


# In[21]:


dfcon.isna().sum()


# In[22]:


#totaluserratings=2499
#unique user ratings=177
dfcon['USERRATINGS'].nunique()


# In[23]:


dfcon['GENRE'].unique()


# In[24]:


dfcon['GENRE'].value_counts().head(5)


# # booksvisithistory

# In[25]:


#booksvist
df4.columns


# In[26]:


#bookid and userid total count==4999
#uniquebookid=2178
#uniqueuserid=3029
df4.shape[0]


# In[27]:


df4.count()


# In[28]:


#frequently previewed books
dffreq=df4[['BookID','BOOKPREVIEWED','SUBSCRIBED']]


# In[29]:


frequent=pd.merge(dffreq,dfcon,on='BookID',how='inner')


# In[30]:


#details and author of 3 most frequently previewed books
frequent[['BookID','BOOKPREVIEWED','AUTHOR']].value_counts().head(30)


# In[31]:


#authors of 30 most subscribed books
frequent[['BookID','SUBSCRIBED','AUTHOR']].value_counts().head(30)


# In[32]:


df4.nunique()


# In[33]:


df4.isna().sum()


# In[34]:


df4['BOOKPREVIEWED'].unique()


# In[35]:


df4['SUBSCRIBED'].unique()


# # books purchase history

# In[36]:


#bookspurchasehistory
df5.columns


# In[37]:


df5['BookID'].nunique()


# In[38]:


df5.count()


# In[39]:


#top 3 authors whose books have been purchased the most
dft=pd.merge(dfcon,df5,on='BookID',how='inner')


# In[40]:


dft[['BookID','AUTHOR']].value_counts().head(30)


# In[77]:


#genre of top 5 books which are commonly purchased the maximum number of times
dft[['BookID','GENRE','SUBSTATE']].value_counts().head(5)


# In[42]:


df5.nunique()


# In[78]:


#top5 substates from where maximum books have been purchased
df5['SUBSTATE'].value_counts().head(5)


# In[44]:


df5.isna().sum()


# # user master

# In[45]:


df6.columns


# In[79]:


df6.describe()


# In[ ]:


d


# In[ ]:





# In[46]:


#unique users----->15000
df6.count()


# In[ ]:


df6


# In[47]:


#---->not sure ----->users who are signed up with total count based on gender and age bw 20-30 and 31-40
df6[['UserID','SIGNUPDATE','AGEGROUP','GENDER']][(df6['AGEGROUP']<30) & (df6['AGEGROUP']>20)]


# In[48]:


df6['GENDER'].value_counts()


# In[49]:


#extract users
df6['UserID'].nunique()


# In[50]:


df6.nunique()


# In[51]:


df6.isna().sum()


# In[52]:


dfcon['DETAILS'][1].replace(',','_')


# In[53]:


dfcon['DETAILS'][1].replace('(','_')
dfcon['DETAILS'][1].replace(')','_')


# In[54]:


punctuations="()[]{}:;, ''\n"
#print(s)


# In[55]:


s=dfcon['DETAILS']
for ch in punctuations:
    
    #print(ch)
    s=s.replace(ch,'_')
s=s.replace('\n','_')
print(s)


# In[56]:


def cleandetails (s1):
    s=s1
    punctuations="()[]{}:;, ''?\n # $-."
    for ch in punctuations:
        s=s.replace(ch,'_')
    return(s)


# In[57]:


dfcon.columns


# In[58]:


#dfcon['DETAILS']=dfcon['DETAILS'].apply(cleandetails)
#dfcon['OTHERPRINTEDINFO']=dfcon['OTHERPRINTEDINFO'].apply(cleandetails)
#dfcon['COVERPAGE']=dfcon['COVERPAGE'].apply(cleandetails)
dfcon['BOOKTITLE']=dfcon['BOOKTITLE'].apply(cleandetails)
dfcon['BOOKNAME']=dfcon['BOOKNAME'].apply(cleandetails)
#dfcon['SERIES']=dfcon['SERIES'].apply(cleandetails)


# In[59]:


dfcon['USERRATINGS'].describe()


# In[60]:


dfcon.head(3)


# In[61]:


regex="[()[]{}:;, ''\n\"]"


# In[62]:


dfcon.to_csv(r"C:\Users\priyakumari56\Documents\capstone project\Capstone6_Book Recommendation\combined.csv",encoding='utf-8')


# In[63]:


import re


# In[64]:


print(s)


# In[65]:


s="[('Original Title', 'Rainbows End'_, ('ISBN', '\\n                  0812536363\\n                      (ISBN13: 9780812536362_\\n                '_, ('Edition Language', 'English'_, ('Literary Awards', '\\n                  Hugo Award for Best Novel (2007_, Locus Award for Best Science Fiction Novel (2007_, John W. Campbell Memorial Award Nominee for Best Novel (2007_, Prometheus Award Nominee for Best Novel (2007_\\n                '_]"


# In[66]:


s1=re.sub(regex,'_',s)
print(s1)


# In[67]:


dfcon['DETAILS'].head(2)


# In[68]:


dfcon['SUMMARY'].head(2)


# In[69]:


dfcon['OTHERPRINTEDINFO'].head(2)


# In[70]:


dfcon['COVERPAGE'].head(2)


# In[ ]:




