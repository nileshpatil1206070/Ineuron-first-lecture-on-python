#!/usr/bin/env python
# coding: utf-8

# # Math operations
# 

# In[1]:


5+7


# In[2]:


7--9


# In[1]:


5/2


# In[2]:


5//2


# In[3]:


1.75*2


# In[4]:


3.5//1.75


# In[5]:


3.5//2


# In[6]:


5%2


# In[7]:


#BODMAS RULE
5+5*3/3


# In[8]:


#use of bracket for math operations
(5+7)*9


# # Data type of i/p or o/p

# In[9]:


#data type of given input or output
type(4/5)


# In[10]:


type('nilesh')


# In[11]:


type(5/1
)


# In[12]:


type(5)


# In[13]:


a=5
b=48
a+b


# In[14]:


type(a+b)


# In[15]:


c=a+b
c


# In[16]:


type(c)


# # Boolean operation

# In[17]:


#boolean opeartions
true


# In[18]:


True


# In[19]:


True or False


# In[20]:


True and False


# In[21]:


True and True


# In[22]:


type(True and False)


# In[23]:


True|False


# In[10]:


a=10
b=5
(a+b>25) | (a-b>1)


# In[4]:


True|False


# In[6]:


True or False


# # Strings
# 

# In[11]:


type('Nilesh')


# In[12]:


type('K')


# In[13]:


type('Nilesh is a truly stoic philosopher')


# In[14]:


type("Stoicism is krishna,marcus aurelius")


# In[2]:


str1 ='nilesh'


# In[3]:


str1


# In[4]:


str('1')


# In[8]:


str1='Nilesh is'
str2='true stoic'
str3=str1+' '+str2
str3


# In[10]:


Name=input('pls enter your name for application in bank')
print(Name)


# In[14]:


a=input('enter first no ')
b=input('enter second no ')
c=int(a)+int(b)
print('the answer is {}'.format(c))


# # string formatting

# In[23]:


first_name=input('enter first name ')
last_name=input('enter last name ')
print('my first name is {first} and my last name is {last}'.format(first=first_name,last=last_name))


# # variable dynamic typing

# In[24]:


a=50
type(a)


# In[25]:


str1='Nilesh'
type(str1)


# In[28]:


print('krish'+str(1))


# In[30]:


1+float("2")


# # conditional statements

# In[35]:


a=int(input('enter first number '))
b=int(input('enter second number '))
c=a-b
print(c)
if c<0:
    print('the answer is negative')
elif c>40:
    print('the difference is huge')
else:
    print('the number is positive')
print('press enter to exit:')


# In[ ]:





# # In-built Data structures
# 
# 1.list
# 2.Tuple
# 3.string
# 4.dictionaries
# 5.sets
# 
# 

# In[3]:


lst=[1,52,35.6,'nilesh','stoic','marcus aurelius']
lst


# In[38]:


lst[3]


# In[39]:


lst[2]


# In[40]:


type(lst[2])


# In[41]:


type(lst)


# In[43]:


lst.append('ryan holiday')


# In[44]:


lst


# In[49]:


lst.append('amor')


# In[6]:


lst.append('amor fati')
lst


# In[7]:


lst[3]='memento mori'
lst


# # string indexing

# In[ ]:





# In[10]:


str1='marcus aurelius'


# In[13]:


#strings are immutable because u cant change their characters


# In[12]:


str1[5]='k'


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


str("25")

