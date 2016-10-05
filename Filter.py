
# coding: utf-8

# Built-In Function Filter

# Filter (Function, list)

# In[2]:

def even_find(number):
    if number%2 ==0:
        return True
    else:
        return False


# In[6]:

l = range(20)
print l


# In[5]:

f = filter(even_find, l)
print f


# In[ ]:



