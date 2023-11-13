#!/usr/bin/env python
# coding: utf-8

# In[72]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import numpy as np


# In[120]:


cast = pd.read_csv("E:/Python docs/cast.csv")
cast.head()


# ### How many movies are listed in the titles dataframe?

# In[85]:


df=pd.DataFrame['title'].count()
print(df)


# In[35]:


print(data.shape)


# ### What are the earliest two films listed in the titles dataframe?

# In[132]:


cast.sort_values(by='year').head(2)


# ### How many movies have the title "Hamlet"?

# In[105]:


len(np.where(pd.DataFrame['title'] == 'Hamlet')[0])


# ### How many movies are titled "North by Northwest"?

# In[134]:


len(cast[cast.title=="North by Northwest"])


# ### When was the first movie titled "Hamlet" made?

# In[137]:


cast[cast.title=="Hamlet"].year.min()


# ### List all of the "Treasure Island" movies from earliest to most recent.

# In[138]:


cast[cast.title=="Treasure Island"].sort_values(by='year')


# ### How many movies were made in the year 1950?

# In[141]:


len(cast[cast.year==1950])


# In[ ]:





# ### How many movies were made in the year 1960?

# In[142]:


len(cast[cast.year==1960])


# In[ ]:





# ### How many movies were made from 1950 through 1959?

# In[144]:


len(cast[(cast.year>=1950) & (cast.year<=1959)])


# In[ ]:





# ### In what years has a movie titled "Batman" been released?

# In[148]:


cast[cast.title=="Batman"].sort_values(by='year')


# In[ ]:





# ### How many roles were there in the movie "Inception"?

# In[150]:


len(cast[cast.title=="Inception"])


# In[ ]:





# ### How many roles in the movie "Inception" are NOT ranked by an "n" value?

# In[152]:


len(cast[(cast.title=="Inception")&(cast.n.isnull())])


# In[ ]:





# ### But how many roles in the movie "Inception" did receive an "n" value?

# In[153]:


len(cast[(cast.title=="Inception")&(cast.n.notnull())])


# In[ ]:





# ### Display the cast of "North by Northwest" in their correct "n"-value order, ignoring roles that did not earn a numeric "n" value.

# In[157]:


cast[(cast.title=="North by Northwest") & (cast.n.notnull())].sort_values(by='n')


# In[ ]:





# ### Display the entire cast, in "n"-order, of the 1972 film "Sleuth".

# In[158]:


cast[(cast.title=="Sleuth") & (cast.year==1972) &(cast.n.notnull())].sort_values(by='n')


# In[ ]:





# ### Now display the entire cast, in "n"-order, of the 2007 version of "Sleuth".

# In[159]:


cast[(cast.title=="Sleuth") & (cast.year==2007) &(cast.n.notnull())].sort_values(by='n')


# In[ ]:





# ### How many roles were credited in the silent 1921 version of Hamlet?

# In[162]:


len(cast[(cast.title=="Hamlet") & (cast.year==1921)])


# In[ ]:





# ### How many roles were credited in Branagh’s 1996 Hamlet?

# In[163]:


len(cast[(cast.title=="Hamlet") & (cast.year==1996)])


# In[ ]:





# ### How many "Hamlet" roles have been listed in all film credits through history?

# In[164]:


len(cast[cast.character=='Hamlet'])


# In[ ]:





# ### How many people have played an "Ophelia"?

# In[165]:


len(cast[cast.character== "Ophelia"])


# In[ ]:





# ### How many people have played a role called "The Dude"?

# In[166]:


len(cast[cast.character== "The Dude"])


# In[ ]:





# ### How many people have played a role called "The Stranger"?

# In[167]:


len(cast[cast.character== "The Stranger"])


# In[ ]:





# ### How many roles has Sidney Poitier played throughout his career?

# In[170]:


len(cast[cast.name== "Sidney Poitier"])


# In[ ]:





# ### How many roles has Judi Dench played?

# In[173]:


len(cast[cast.name=="Judi Dench"])


# In[ ]:





# ### List the supporting roles (having n=2) played by Cary Grant in the 1940s, in order by year.

# In[176]:


cast[(cast.name =="Cary Grant")& (cast.year// 10==194)&(cast.n ==2)].sort_values(by='year')


# In[ ]:





# ### List the leading roles that Cary Grant played in the 1940s in order by year.

# In[177]:


cast[(cast.name =="Cary Grant")& (cast.year// 10==194)].sort_values(by='year')


# In[ ]:





# ### How many roles were available for actors in the 1950s?

# In[181]:


len(cast[(cast.type =="actor")& (cast.year// 10==195)])


# In[ ]:





# ### How many roles were available for actresses in the 1950s?

# In[182]:


len(cast[(cast.type =="actress")& (cast.year// 10==195)])


# In[ ]:





# ### How many leading roles (n=1) were available from the beginning of film history through 1980?

# In[183]:


len(cast[(cast.year ==1980)& (cast.n==1)])


# In[ ]:





# ### How many non-leading roles were available through from the beginning of film history through 1980?

# In[184]:


len(cast[(cast.year ==1980)& (cast.n!=1)])


# In[ ]:





# ### How many roles through 1980 were minor enough that they did not warrant a numeric "n" rank?

# In[185]:


len(cast[(cast.year <=1980)& (cast.n.isnull())])


# In[ ]:




