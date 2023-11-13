#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd


# In[17]:


titles = pd.read_csv('E:\Python docs/titles.csv')
titles.head()


# In[34]:


cast = pd.read_csv('E:\Python docs/cast.csv')
cast.head()


# In[ ]:





# ### What are the ten most common movie names of all time?

# In[20]:


titles.title.value_counts().head(10)


# In[ ]:





# ### Which three years of the 1930s saw the most films released?

# In[21]:


titles[titles.year //10 ==193].year.value_counts().head(3)


# In[ ]:





# ### Plot the number of films that have been released each decade over the history of cinema.

# In[29]:


titles['decade']=((titles.year // 10) *10)
titles.decade.value_counts().sort_index().plot(kind="bar")


# In[ ]:





# ### Plot the number of "Hamlet" films made each decade.

# In[30]:


titles['decade']=((titles.year // 10) *10)
titles[titles.title=="Hamlet"].decade.value_counts().sort_index().plot(kind="bar")


# In[ ]:





# ### Plot the number of "Rustler" characters in each decade of the history of film.

# In[37]:


cast['decade']=((cast.year // 10) *10)
cast[cast.character=="Rustler"].decade.value_counts().sort_index().plot(kind="bar")


# In[ ]:





# ### Plot the number of "Hamlet" characters each decade.

# In[38]:


cast['decade']=((cast.year // 10) *10)
cast[cast.character=="Hamlet"].decade.value_counts().sort_index().plot(kind="bar")


# In[ ]:





# ### What are the 11 most common character names in movie history?

# In[39]:


cast.character.value_counts().head(11)


# In[ ]:





# ### Who are the 10 people most often credited as "Herself" in film history?

# In[40]:


cast[cast.character=="Herself"].name.value_counts().head(10)


# In[ ]:





# ### Who are the 10 people most often credited as "Himself" in film history?

# In[41]:


cast[cast.character=="Himself"].name.value_counts().head(10)


# In[ ]:





# ### Which actors or actresses appeared in the most movies in the year 1945?

# In[42]:


cast[cast.year == 1945].name.value_counts().head(10)


# In[ ]:





# ### Which actors or actresses appeared in the most movies in the year 1985?

# In[43]:


cast[cast.year == 1985].name.value_counts().head(10)


# In[ ]:





# ### Plot how many roles Mammootty has played in each year of his career.

# In[45]:


cast[cast.character=="Mammootty"].year.value_counts().sort_index().plot(kind="bar")


# In[ ]:





# ### What are the 10 most frequent roles that start with the phrase "Patron in"?

# In[46]:


ph=cast[cast.character.str.startswith("Patron in")]
ph.character.value_counts().head(10)


# In[ ]:





# ### What are the 10 most frequent roles that start with the word "Science"?

# In[47]:


sc=cast[cast.character.str.startswith("Science")]
sc.character.value_counts().head(10)


# In[ ]:





# ### Plot the n-values of the roles that Judi Dench has played over her career.

# In[65]:


a=cast[cast.name=="Judi Dench"]
a.n.value_counts().sort_index().plot(kind="bar")


# In[55]:


x.n.value_counts()


# In[70]:


a.plot(kind="scatter",x="year",y="n", s= 0.5)


# In[ ]:





# ### Plot the n-values of Cary Grant's roles through his career.

# In[64]:


b=cast[cast.name=="Cary Grant"]
b.n.value_counts().sort_index().plot(kind="bar")


# ### Plot the n-value of the roles that Sidney Poitier has acted over the years.

# In[72]:


cast[cast.name=="Sidney Poitier"].plot(kind="scatter",x="year",y="n")


# In[73]:


cast[cast.name=="Sidney Poitier"].n.value_counts()


# ### How many leading (n=1) roles were available to actors, and how many to actresses, in the 1950s?

# In[74]:


cast[(cast.year//10==195)&(cast.n==1)].type.value_counts()


# In[ ]:





# ### How many supporting (n=2) roles were available to actors, and how many to actresses, in the 1950s?

# In[75]:


cast[(cast.year//10==195)&(cast.n==2)].type.value_counts()


# In[ ]:




