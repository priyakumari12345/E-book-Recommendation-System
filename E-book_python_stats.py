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


# In[3]:


dfcon=pd.concat([df2,df3],axis=0)
dfcon.drop(['AUTHORDESC','DETAILS','OTHERPRINTEDINFO','GENRE.1','SUMMARY','COVERPAGE'],axis=1,inplace=True)


# In[284]:


dfcon_purchase=pd.merge(df5,dfcon,on='BookID',how='inner')
dfcon_visit=pd.merge(dfcon,df4,on='BookID',how='inner')
dfcon_user_visit=pd.merge(dfcon_visit,df6,on='UserID',how='inner')
dfcon_user_purchase=pd.merge(dfcon_purchase,df6,on='UserID',how='inner')
dfcon_user=pd.merge(dfcon_purchase,df6,on='UserID',how='inner')
user_visit=pd.merge(df6,df4,on='UserID',how='inner')


# In[50]:


dfcon_user_purchase.head(1)


# In[49]:


dfcon_user_purchase.drop(['DELETED','WeekofYear'],axis=1,inplace=True)


# ## AVERAGE AGE GROUP AND CORRESPONDING RATING GIVEN BY USERS

# In[7]:


dfcon_user[['USERRATINGS','AGEGROUP']].groupby(dfcon_user['GENRE']).mean().sort_values(by='USERRATINGS',ascending=False)


# ### Percentage of users in each age bracket

# In[79]:


users=df6['UserID'].value_counts().sum()
users


# In[26]:


age15to25=df6['AGEGROUP'][(df6['AGEGROUP']>=15) & (df6['AGEGROUP']<=25)].groupby(df6['AGEGROUP']).value_counts().sum()
(age15to25/users)*100


# In[27]:


age25to35=df6['AGEGROUP'][(df6['AGEGROUP']>25) & (df6['AGEGROUP']<=35)].groupby(df6['AGEGROUP']).value_counts().sum()
(age25to35/users)*100


# In[28]:


age35to45=df6['AGEGROUP'][(df6['AGEGROUP']>35) & (df6['AGEGROUP']<=45)].groupby(df6['AGEGROUP']).value_counts().sum()
(age35to45/users)*100


# In[29]:


age45to55=df6['AGEGROUP'][(df6['AGEGROUP']>45) & (df6['AGEGROUP']<=55)].groupby(df6['AGEGROUP']).value_counts().sum()
(age45to55/users)*100


# In[30]:


age55to65=df6['AGEGROUP'][(df6['AGEGROUP']>55) & (df6['AGEGROUP']<=65)].groupby(df6['AGEGROUP']).value_counts().sum()
(age55to65/users)*100


# In[31]:


age65to75=df6['AGEGROUP'][(df6['AGEGROUP']>65) & (df6['AGEGROUP']<=75)].groupby(df6['AGEGROUP']).value_counts().sum()
(age65to75/users)*100


# In[32]:


age75to80=df6['AGEGROUP'][(df6['AGEGROUP']>75) & (df6['AGEGROUP']<=80)].groupby(df6['AGEGROUP']).value_counts().sum()
(age75to80/users)*100


# ### Most purchased books and its author by users in age bracket 25-55 each

# In[92]:


dfcon_user[['GENRE','AUTHOR']][(dfcon_user['AGEGROUP']>35) & (dfcon_user['AGEGROUP']<=45)].value_counts().head(4)


# In[89]:


dfcon_user[['GENRE','AUTHOR']][(dfcon_user['AGEGROUP']>25) & (dfcon_user['AGEGROUP']<=35)].value_counts().head(4)


# In[93]:


dfcon_user[['GENRE','AUTHOR']][(dfcon_user['AGEGROUP']>45) & (dfcon_user['AGEGROUP']<=55)].value_counts().head(4)


# In[94]:


dfcon_user[['GENRE','AUTHOR']][(dfcon_user['AGEGROUP']>35) & (dfcon_user['AGEGROUP']<=45)].value_counts().head(4)


# In[104]:


dfcon_user[['GENRE','AUTHOR','USERRATINGS']][(dfcon_user['AGEGROUP']>35) & (dfcon_user['AGEGROUP']<=45)].value_counts().head(15)


# In[105]:


dfcon['USERRATINGS'].mean()


# In[95]:


dfcon_user[['GENRE','AUTHOR']][(dfcon_user['AGEGROUP']>25) & (dfcon_user['AGEGROUP']<=35)].value_counts().head(4)


# In[101]:


dfcon_user[['GENRE','AUTHOR','USERRATINGS']][(dfcon_user['AGEGROUP']>25) & (dfcon_user['AGEGROUP']<=35)].value_counts().head(10)


# In[100]:


dfcon_user[['GENRE','AUTHOR']][(dfcon_user['AGEGROUP']>45) & (dfcon_user['AGEGROUP']<=55)].value_counts().head(5)


# In[99]:


dfcon_user[['GENRE','AUTHOR','USERRATINGS']][(dfcon_user['AGEGROUP']>45) & (dfcon_user['AGEGROUP']<=55)].value_counts().head(10)


# # ttest ||Eg1 || 1 sample 2 tailed)

# In[134]:


avgrating_by_genre=dfcon_user[['USERRATINGS']].groupby(dfcon_user['GENRE']).mean().sort_values(by='USERRATINGS',ascending=False)
avg_rating=avgrating_by_genre['USERRATINGS']


# In[148]:


if len(avg_rating)<30:
    print("Can do t-test")


# H0:mu is 3.92
# H1:mu is not 3.92 ==>it is 1 sampled 2 tailed test. we will compare alpha with pvalue_tt

# In[139]:


population_mean=avg_rating.mean()
alpha=0.01


# In[149]:


import random
random_sample_userrating=random.choices(avg_rating.round(2), k= 10)


# In[145]:


from scipy.stats import ttest_1samp
tstatistic, pvalue_tt = ttest_1samp(random_sample_userrating,population_mean)


# In[146]:


if pvalue_tt < alpha:
    print("Reject the null hypothesis")
else:
    print("Failed to reject the null hypothesis")


# ### Eg 2 || 1 sample left tailed test

# In[274]:


population_mean=df6['AGEGROUP'].mean()
data=df6['AGEGROUP'].to_list()


# H0:average age group is 42
# H1:average age group is less than 42

# In[282]:


alpha=-0.01 #since it is left tailed test
import random
random_sample=random.choices(data, k= 10)
from scipy.stats import ttest_1samp
tstatistic, pvalue_tt = ttest_1samp(random_sample,population_mean)
pvalue_lt=pvalue_tt/2


# In[283]:


if pvalue_lt < alpha:
    print("Reject the null hypothesis")
else:
    print("Failed to reject the null hypothesis")


# Thus we can say with 99% confidence that average age group is 42 

# ### Eg 3||  1 sample right tailed test

# #most subscribed book is of genre type fiction . Let's check whether its average rating is more than 4 or not
# H0:rating is less than,equal to 4
# H1: rating is more than 4----->implies right tailed test

# In[318]:


rating_fiction=dfcon[['GENRE','USERRATINGS']][dfcon['GENRE']=='Fiction'].value_counts()
len(rating_fiction)
data=dfcon['USERRATINGS'].to_list()


# In[306]:


population_mean=dfcon['USERRATINGS'].mean()
population_mean


# In[321]:


alpha=0.01 #since it is right tailed test
import random
random_sample=random.choices(data, k= 30)
from scipy.stats import ttest_1samp
tstatistic, pvalue_tt = ttest_1samp(random_sample,population_mean)
pvalue_rt=pvalue_tt/2


# In[322]:


if pvalue_lt < alpha:
    print("Reject the null hypothesis")
else:
    print("Failed to reject the null hypothesis")


# Thus we can say with 99% confidence that average rating given to Fiction books is less than 4

# # chi2 test

# ### eg1------->H0: Most subscribed book is of genre Fiction

# In[227]:


dfcon_visit[['GENRE','SUBSCRIBED']][dfcon_visit['SUBSCRIBED']==1].value_counts()


# In[301]:


alpha=0.05
contingency=pd.crosstab(dfcon_visit['GENRE'],dfcon_visit['SUBSCRIBED'])
from scipy.stats import chi2_contingency
chi2, p, dof, expected = chi2_contingency(contingency)
#print(chi2, p, dof, expected)


# In[239]:


if p<alpha:
    print("Reject null hypothesis")
else:
    print("Failed to reject null hypothesis")


# Thus we can say with 95% confidence that most subscribed book is of genre type Fiction

# ### eg2------->H0: Children's book is top rated book on an average

# In[250]:


toprated=dfcon[['GENRE','USERRATINGS']].groupby(dfcon['GENRE']).mean().sort_values(by='USERRATINGS',ascending=False)


# In[300]:


alpha=0.01
contingency=pd.crosstab(dfcon['GENRE'],dfcon['USERRATINGS'])
from scipy.stats import chi2_contingency
chi2, p, dof, expected = chi2_contingency(contingency)
#print(chi2, p, dof, expected)


# In[255]:


if p<alpha:
    print("Reject null hypothesis")
else:
    print("Failed to reject null hypothesis")


# Thus with 99% confidence we can say Children's book is not top rated book on an average

# ### eg3------->most books are subscribed from California state

# In[299]:


mostsubs_by_state=user_visit[['STATE','SUBSCRIBED']][user_visit['SUBSCRIBED']==1].value_counts()
len(mostsubs_by_state)


# In[296]:


alpha=0.01
contingency=pd.crosstab(user_visit['STATE'],user_visit['SUBSCRIBED'])
from scipy.stats import chi2_contingency
chi2, p, dof, expected = chi2_contingency(contingency)
#print(chi2, p, dof, expected)


# In[297]:


if p<alpha:
    print("Reject null hypothesis")
else:
    print("Failed to reject null hypothesis")


# Thus we can say with 99% confidence that most users are from California state

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




