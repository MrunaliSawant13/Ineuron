#!/usr/bin/env python
# coding: utf-8

# 1. What exactly is []?
# 
# ANS: This is an empty list(List with no values).

# ________________________________________________________________________________________________________________________________

# 2. In a list of values stored in a variable called spam, how would you assign the value &#39;hello&#39; as the
# third value? (Assume [2, 4, 6, 8, 10] are in spam.)

# In[3]:


spam = [2,4,6,8,10]

spam[2] = 'hello'


# In[4]:


spam


# ________________________________________________________________________________________________________________________________

# Let's pretend the spam includes the list [&#39;a&#39;, &#39;b&#39;, &#39;c&#39;, &#39;d&#39;] for the next three queries.

# In[5]:


spam = ['a', 'b', 'c', 'd']


# 3. What is the value of spam[int(int(&#39;3&#39; * 2) / 11)]? 
# 
# It will give the value at index 3 as follows:

# In[9]:


spam[int(int('3' * 2) / 11)]


# ________________________________________________________________________________________________________________________________

# 4. What is the value of spam[-1]?
# 
# This will return last value as follows:

# In[11]:


spam[-1]


# ________________________________________________________________________________________________________________________________

# 5. What is the value of spam[:2]?
# 
# This will return values in spam at index 0 and 1

# In[13]:


spam[:2]


# ________________________________________________________________________________________________________________________________

# Let&#39;s pretend bacon has the list [3.14, &#39;cat,&#39; 11, &#39;cat,&#39; True] for the next three questions.

# In[20]:


bacon = [3.14, 'cat', 11, 'cat', True]


# 6. What is the value of bacon.index(&#39;cat&#39;)?
# 
# This will return the first index at which 'cat' occured

# In[22]:


bacon.index('cat')


# ________________________________________________________________________________________________________________________________

# How does bacon.append(99) change the look of the list value in bacon?
# 
# This will add 99 at the end of the bacon list and this increase the size of it

# In[33]:


bacon.append(99)


# In[34]:


bacon


# ________________________________________________________________________________________________________________________________

# 8. How does bacon.remove(&#39;cat&#39;) change the look of the list in bacon?
# 
# This removes the first occurance of 'cat' in bacon list and thus reduces its size
# 

# In[37]:


bacon.remove('cat')


# In[36]:


bacon


# ________________________________________________________________________________________________________________________________
# 

# 9. What are the list concatenation and list replication operators?
# 
# ANS: list concatenation operator is +
#     
#     list replication operator is *
# 
# 

# ________________________________________________________________________________________________________________________________

# 10. What is difference between the list methods append() and insert()?
# 
# ANS: append() will add element at the end of the list. While, using insert() we can specify at which position/index the element is to be added

# ________________________________________________________________________________________________________________________________

# 11. What are the two methods for removing items from a list?
# 
# ANS: pop() can be used to remove last element in the list.
# 
# remove() can be used to remove specific element in the list.
# 
# clear() will remove all the elements in the list

# ________________________________________________________________________________________________________________________________

# 12. Describe how list values and string values are identical.
# 
# ANS: Both list and string can be passed to len(), they both have indexes and slices, they can be used in for loops, they can be concatenated or replicated, and they both can be used with the in and not in operators.

# ________________________________________________________________________________________________________________________________

# 13. What&#39;s the difference between tuples and lists?
# 
# ANS: Lists are mutable and tuples are immutable. That means, the list values can be changed, removed, added, etc but these operations are not possible for tuples.
# 

# ________________________________________________________________________________________________________________________________

# 14. How do you type a tuple value that only contains the integer 42?

# simply as: (42,)
# 
# or if we consider a tuple name valueme:
# valueme = (42,)

# ________________________________________________________________________________________________________________________________

# 15. How do you get a list value&#39;s tuple form? How do you get a tuple value&#39;s list form?

# ANS:
# 
# We can use tuple() and list() functions respectively.
# 
# For example:

# In[49]:


b = tuple([1,2,3])


# In[50]:


type(b)


# In[47]:


valueme = list((42,2))


# In[48]:


type(valueme)


# ________________________________________________________________________________________________________________________________

# 16. Variables that &quot;contain&quot; list values are not necessarily lists themselves. Instead, what do they
# contain?

# These variables contain references of list values

# ________________________________________________________________________________________________________________________________
# 

# 17. How do you distinguish between copy.copy() and copy.deepcopy()?

# The copy.copy() generates reference to original object, thus while changing new object original object is also changed. While, deepcopy() will copy of original object to new one

# In[ ]:




